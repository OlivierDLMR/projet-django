from datetime import date, timedelta
from pprint import pprint

import requests


def get_rates(currencies, days=30):
    end_date = date.today()
    star_date = end_date - timedelta(days=days)
    # end_date = end_date.strftime("%Y-%m-%d")
    # star_date = star_date.strftime("%Y-%m-%d")

    symbols = ','.join(currencies)
    requete = f"https://api.exchangeratesapi.io/history?start_at={star_date}&end_at={end_date}&symbols={symbols}"
    r = requests.get(requete)
    if not r and not r.json():
        return False, False


    api_rates = r.json().get("rates")
    # créer un dictionnaire
    all_rates = {currency: [] for currency in currencies}
    # va créer un dictionnaire {'CAD': [], 'USD': [] }
    #pprint(all_rates)
    all_days = sorted(api_rates.keys())

    for each_day in all_days:
        # 1er element currency la clé et le 2eme rate la valeur
        [all_rates[currency].append(rate) for currency, rate in api_rates[each_day].items()]



    return all_days, all_rates


if __name__ == '__main__':
    days, rates = get_rates(currencies=["USD", "CAD"])
    pprint(days)
    pprint(rates)
