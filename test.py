import threading

def reloadCurrencys():
    print(str("sa"))

threading.Timer(2.0, reloadCurrencys).start()