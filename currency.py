#exchange rate from USD to INR
exchange_rate = 85  

def convert_usd_to_inr(amount):
   
    return amount * exchange_rate

def main():
    print("USD to INR Currency Converter")

    amount = float(input("Enter the amount in USD: "))

    result = convert_usd_to_inr(amount)
    print({amount}, "USD is equal to", {result},"INR")

if __name__ == "__main__":
    main()