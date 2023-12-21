import requests

headers = {
    'apikey': 'API KEY HERE'
}
def GetInfo(From,To):

    response = (requests.request("GET", "https://api.currencyapi.com/v3/latest",headers=headers)).json()

    Codes ={'AED (United Arab Emirates Dirham)': 'AED', 'ARS (Argentine Peso)': 'ARS', 'AUD (Australian Dollar)': 'AUD', 'EUR (Euro)': 'EUR', 'BGN (Bulgarian Lev)': 'BGN', 'BMD (Bermudian Dollar)': 'BMD', 'BRL (Brazilian Real)': 'BRL', 'CAD (Canadian Dollar)': 'CAD', 'CHF (Swiss Franc)': 'CHF', 'CLP (Chilean Peso)': 'CLP', 'CNY (Chinese Renminbi)': 'CNY', 'COP (Colombian Peso)': 'COP', 'CZK (Czech Koruna)': 'CZK', 'DKK (Danish Krona)': 'DKK', 'EGP (Egyptian Pound)': 'EGP', 'GBP (British Pound)': 'GBP', 'HKD (Hong Kong Dollar)': 'HKD', 'HRK (Croatian kuna)': 'HRK', 'HUF (Hungarian Forint)': 'HUF', 'IDR (Indonesian Rupiah)': 'IDR', 'INR (Indian Rupee)': 'INR', 'ILS (Israeli Shekel)': 'ILS', 'JMD (Jamaican Dollar)': 'JMD', 'JPY (Japanese Yen)': 'JPY', 'KZT (Tenge)': 'KZT', 'KRW (South Korean won)': 'KRW', 'MXN (Mexican Peso)': 'MXN', 'MYR (Malaysian Ringgit)': 'MYR', 'NGN (Nigerian Naira)': 'NGN', 'NOK (Norwegian Krona)': 'NOK', 'NZD (New-Zealand Dollar)': 'NZD', 'PEN (Peruvian New Sol)': 'PEN', 'PHP (Philippines Peso)': 'PHP', 'PLN (Polish Zloty)': 'PLN', 'QAR (Qatari Riyal)': 'QAR', 'RON (Romanian Leu)': 'RON', 'RUB (Russian Ruble)': 'RUB', 'SAR (Saudi Riyal)': 'SAR', 'SGD (Singapore Dollar)': 'SGD', 'SEK (Swedish Krona)': 'SEK', 'THB (Thai Baht)': 'THB', 'TTD (Trinidad and Tobago Dollar)': 'TTD', 'TRY (Turkish Lira)': 'TRY', 'TWD (Taiwan Dollar)': 'TWD', 'UAH (Ukrainian Hryvnia)': 'UAH', 'USD (US Dollar)': 'USD', 'VND (Vietnamese Dong)': 'VND', 'ZAR (South African Rand)': 'ZAR'}
    
    From = Codes[From]
    To = Codes[To]

    Rate1 = response['data'][From]['value']
    Rate2 = response['data'][To]['value']
    return Rate1, Rate2


def Convert(Amt, From, To):
    Rate1, Rate2 = GetInfo(From, To)
    Usd_Amt = float(Amt) / Rate1
    Rate2_Amt = round(Usd_Amt * Rate2,3)
    return Rate2_Amt


#print(Convert(7548,'AUD (Australian Dollar)','SGD (Singapore Dollar)'))