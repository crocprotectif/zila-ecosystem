import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
SECRET_KEY = os.getenv("SECRET_KEY")

RPC_URL = os.getenv("RPC_URL")

ROUTER = os.getenv("ROUTER")
WETH = os.getenv("WETH")

ZILA_TOKEN = os.getenv("ZILA_TOKEN")
FEE_PERCENT = float(os.getenv("FEE_PERCENT"))
