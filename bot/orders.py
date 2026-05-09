from binance.exceptions import BinanceAPIException
import logging

logger = logging.getLogger("TradingBot")

def place_futures_order(client, symbol, side, order_type, quantity, price=None):
    """Sends the order request to Binance Futures Testnet."""
    try:
        # Prepare parameters
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
        }

        # For LIMIT orders, we need price and timeInForce
        if order_type.upper() == "LIMIT":
            params["price"] = str(price)
            params["timeInForce"] = "GTC"  # GTC = Good Till Cancelled

        logger.info(f"Sending {order_type} {side} order for {symbol}...")
        
        # We use futures_create_order specifically for USDT-M Futures
        response = client.futures_create_order(**params)
        
        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.message} (Status Code: {e.status_code})")
        raise Exception(f"Binance Error: {e.message}")
    except Exception as e:
        logger.error(f"Unexpected Error: {str(e)}")
        raise Exception(f"Order failed: {str(e)}")