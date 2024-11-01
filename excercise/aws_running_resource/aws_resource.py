from flask import Flask, render_template
import boto3
import os

template_folder = 'template'
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), template_folder))


def list_running_resources():
    regions = ['us-east-1', 'ap-south-1']
    resources = {
        'EC2': [],
        'ECS': []
    }
    for region in regions:
        session = boto3.Session(region_name=region)

        ec2 = session.client('ec2')
        ec2_instances = ec2.describe_instances()
        for reservation in ec2_instances['Reservations']:
            for instance in reservation['Instances']:
                tags = instance.get('Tags', [])
                name_tag = next((tag['Value'] for tag in tags if tag['Key'] == 'Name'), None)

                region_ec2 = instance.get('PublicDnsName', '')
                if region_ec2:
                    split = region_ec2.split('.')
                    ec2_region = split[1] if len(split) > 1 else 'N/A'
                else:
                    ec2_region = 'N/A'

                if name_tag and name_tag.startswith('robogebra'):
                    resources['EC2'].append({
                        'Name': name_tag,
                        'State': instance['State']['Name'],
                        'Public IP': instance.get('PublicIpAddress', 'N/A'),
                        'VPC ID': instance.get('VpcId', 'N/A'),
                        'Public DNS Name': instance.get('PublicDnsName', 'N/A'),
                        'Region': ec2_region
                    })

    suffixes = ('-dev', '-test')

    for region in regions:
        session = boto3.Session(region_name=region)
        ecs = session.client('ecs')

        ecs_clusters = ecs.list_clusters()
        for cluster_arn in ecs_clusters['clusterArns']:
            cluster_name = cluster_arn.split('/')[-1]

            if cluster_name.endswith(suffixes):
                seen_tasks = set()

                tasks = ecs.list_tasks(cluster=cluster_arn, desiredStatus='RUNNING')
                for task_arn in tasks['taskArns']:
                    task_details = ecs.describe_tasks(cluster=cluster_arn, tasks=[task_arn])

                    for task in task_details['tasks']:
                        task_def_arn = task['taskDefinitionArn']
                        task_def = ecs.describe_task_definition(taskDefinition=task_def_arn)

                        task_identifier = (
                        task_def['taskDefinition']['family'], task_def['taskDefinition']['revision'])

                        if task_identifier not in seen_tasks:
                            seen_tasks.add(task_identifier)

                            for container_def in task_def['taskDefinition']['containerDefinitions']:
                                image = container_def['image']
                                if ':' in image:
                                    image_name, image_tag = image.rsplit(':', 1)
                                else:
                                    image_name, image_tag = image, 'latest'

                                resources['ECS'].append({
                                    'Cluster Name': cluster_name,
                                    'Task Definition': task_def['taskDefinition']['family'],
                                    'Container Name': container_def['name'],
                                    'Image Name': image_name,
                                    'Image Tag': image_tag
                                })

    return resources


@app.route('/')
def index():
    running_resources = list_running_resources()
    return render_template('resources.html', resources=running_resources)


if __name__ == "__main__":
    app.run(debug=True)
