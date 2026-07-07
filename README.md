from fastapi import FastAPI
from strategy import ThreeCandleStrategy
from iq_connection import IQConnection

app = FastAPI()

strategy = ThreeCandleStrategy()
iq = IQConnection()

iq.connect()

@app.get("/")
def home():
    return {
        "status": "online",
        "strategy": "3 Velas"
    }

@app.get("/signal")
def signal():

    candles = iq.get_candles()

    result = strategy.analyze(candles)

    if result:
        return result

    return {
        "signal": None
    }
