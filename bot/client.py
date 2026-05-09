import os
from binance.client import Client
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

def get_binance_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        raise ValueError("API Keys not found. Check your .env file.")

    # testnet=True is critical for using the Testnet URL
    return Client(api_key, api_secret, testnet=True)