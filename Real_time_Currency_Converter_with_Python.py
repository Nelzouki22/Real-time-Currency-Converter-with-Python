import requests

def get_exchange_rate(api_key, from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200:
        print("Error:", data.get("error-type", "Unknown error"))
        return None
    
    exchange_rate = data["conversion_rates"].get(to_currency)
    if exchange_rate is None:
        print(f"Exchange rate for {to_currency} not found.")
        return None
    
    return exchange_rate

def convert_currency(api_key, from_currency, to_currency, amount):
    exchange_rate = get_exchange_rate(api_key, from_currency, to_currency)
    if exchange_rate is None:
        return None
    return amount * exchange_rate

if __name__ == "__main__":
    api_key = "your_api_key_here"  # Replace with your actual API key
    from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()
    amount = float(input("Enter the amount you want to convert: "))
    
    converted_amount = convert_currency(api_key, from_currency, to_currency, amount)
    if converted_amount is not None:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")


