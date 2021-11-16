import requests
import datetime
import json


def get_info(name):

    url1 = r'https://iss.moex.com/cs/engines/stock/markets/shares/boardgroups/57/securities/{}.hs?' \
           r's1.type=candles&interval=4&candles=500&indicators=&_=1637070281775'.format(name)

    url2 = r'https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/{}.jsonp?' \
           r'&iss.meta=off&iss.only=securities%2Cmarketdata%2Cmarketdata_yields&lang=ru&_=1637073061886'.format(name)

    try:
        r = requests.get(url1)
        h = r.json()['candles'][0]['data']
        r.close()
    except json.decoder.JSONDecodeError:
        return None

    c2018, c2019 = 0, 0
    for i in range(len(h)):

        d = datetime.datetime.fromtimestamp(h[i][0] / 1e3)
        if d.year == 2018 and d.month == 1:
            c2018 = h[i][1]
        elif d.year == 2019 and d.month == 1:
            c2019 = h[i][4]

    r = requests.get(url2)
    cap = r.json()['marketdata']['data'][0][-5]
    r.close()

    if None in (c2018, c2019, cap) or 0 in (c2018, c2019, cap):
        return None

    return name, c2018, c2019, cap


def average_array(array, k):

    sum, num = 0, 0
    result_array = []

    for i in range(min(len(array), k)):
        sum += array[i]
        num += 1

    for i in range(len(array)):

        if i - k > 0:
            sum -= array[i - k - 1]
            num -= 1

        if i + k < len(array):
            sum += array[i + k]
            num += 1

        result_array.append(sum / num)

    return result_array
