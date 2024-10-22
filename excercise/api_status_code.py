import requests

while True:
    inputs = input("Enter valid api url: ")
    response = requests.get(inputs)
    print(response.status_code)
    next_calc = input("Do you want to search another api url? (yes/no): ").lower()
    if next_calc != 'yes':
        break


