import pyupbit

access = "s68kyjRJeEeiu4XKR8TasYnfGYqBeoYsULoUxnJW"
secret = "JDg26BlqoxwxPL6hWVgZmEIkGx33ZiZaGOlYaAzM"
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-SAND"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

coin_list = ["KRW-ETH", "KRW-BTC", "KRW-SAND"]

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]


def holding_ratio(ticker):
    holding_amount = get_balance(ticker[4:]) * get_current_price(ticker)
    total_amount = get_balance("KRW")

    for k in coin_list:
        total_amount = total_amount + (get_balance(k[4:]) * get_current_price(k))
    
    ratio = holding_amount / total_amount

    return ratio

def total_seed():
    seed = get_balance("KRW")

    for k in coin_list:
        seed = seed + (get_balance(k[4:]) * get_current_price(k))

    return seed


a = holding_ratio("KRW-SAND")
print(a)