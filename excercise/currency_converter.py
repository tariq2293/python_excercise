class CurrencyConverter:
    rates = {
        "INR": 1, "USD": 83.97, "UAE": 22.86, "THB": 2.5, "SGD": 64.18,
        "SAR": 22.36, "PKR": 0.30, "MYR": 19.56, "CNY": 11.86,
        "AUD": 56.45, "EUR": 91.81, "KWD": 273.98
    }

    def __init__(self, amt, cur):
        self.amt = int(input("Enter Amount : "))
        self.cur = cur

    def bought(self, to_cur):
        if to_cur in self.rates and self.cur in self.rates:

            inr_amt = self.amt * self.rates[self.cur]
            conv_amt = inr_amt / self.rates[to_cur]
            print(f"{self.amt:.2f} {self.cur} is {conv_amt:.2f} {to_cur}")
            self.amt = conv_amt
            self.cur = to_cur
            return conv_amt
        else:
            print("Invalid currency")
            return None

    def seller(self, to_cur):
        if to_cur in self.rates and self.cur in self.rates:
            inr_amt = self.amt * self.rates[self.cur]
            conv_amt = inr_amt / self.rates[to_cur]
            print(f"Selling {self.amt:.2f} {self.cur} gives you {conv_amt:.2f} {to_cur}")
            self.amt = conv_amt
            self.cur = to_cur
            return conv_amt
        else:
            print("Invalid currency")
            return None

    def looped(self):
        for i in self.rates:
            converter.seller(i)


converter = CurrencyConverter(25000, "USD")
converter.looped()


