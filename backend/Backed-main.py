from fastapi import FastAPI
from strategy import ThreeCandleStrategy

app = FastAPI(title="Binary Signal API")

strategy = ThreeCandleStrategy()

# Dados de exemplo (depois serão substituídos pelos candles da IQ Option)
candles = [
    {"open": 1.1000, "close": 1.1010},
    {"open": 1.1010, "close": 1.1020},
    {"open": 1.1020, "close": 1.1030},
]

@app.get("/")
def home():
    return {
        "status": "online",
        "app": "Binary Signal"
    }

@app.get("/signal")
def signal():
    result = strategy.analyze(candles)

    if result:
        return {
            "status": "signal",
            "data": result
        }

    return {
        "status": "waiting",
        "message": "Nenhum sinal encontrado."
    }
