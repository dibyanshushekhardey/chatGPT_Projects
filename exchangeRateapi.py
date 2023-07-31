import requests

def get_exchange_rates(base_currency):
    # Make a request to the Currency API to get the latest exchange rates
    url = f"https://api.currency.com/latest?access_key=p6ST2oTQNt1nNNhgx6XfvZMHDJwXJfV10L4hSOsP&base=USD"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rates = data["rates"]
        return rates
    else:
        print("Failed to retrieve exchange rates.")
        return None

def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Invalid currency.")
        return None

    from_rate = exchange_rates[from_currency]
    to_rate = exchange_rates[to_currency]

    converted_amount = amount * (to_rate / from_rate)
    return converted_amount

def main():
    print("Welcome to Currency Converter!")

    # Prompt the user for the conversion details
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency code: ").upper()
    to_currency = input("Enter the target currency code: ").upper()

    # Get the latest exchange rates
    exchange_rates = get_exchange_rates(from_currency)
    if exchange_rates is None:
        return

    # Perform the currency conversion
    converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
    if converted_amount is None:
        return

    # Display the result
    print(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

if __name__ == '__main__':
    main()
