import argparse
import sys
from bot.client import get_binance_client
from bot.orders import place_futures_order
from bot.validators import validate_order_input
from bot.logging_config import setup_logging

# Initialize Logging
logger = setup_logging()

def main():
    # Setup CLI Arguments
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Simplified Bot")
    parser.add_argument("--symbol", type=str, required=True, help="e.g., BTCUSDT")
    parser.add_argument("--side", type=str, required=True, choices=["BUY", "SELL"], help="BUY or SELL")
    parser.add_argument("--type", type=str, required=True, choices=["MARKET", "LIMIT"], help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Amount to trade")
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        # 1. Validate Input
        validate_order_input(args.symbol, args.side, args.type, args.quantity, args.price)

        # 2. Get Client
        client = get_binance_client()

        # 3. Log the Request Summary
        request_summary = f"Attempting {args.type} {args.side} {args.quantity} {args.symbol} at {args.price if args.price else 'Market Price'}"
        print(f"\n[REQUEST] {request_summary}")
        logger.info(request_summary)

        # 4. Place the Order
        response = place_futures_order(
            client, args.symbol, args.side, args.type, args.quantity, args.price
        )

        # 5. Extract and Print Response Details
        order_id = response.get('orderId')
        status = response.get('status')
        executed_qty = response.get('executedQty')
        avg_price = response.get('avgPrice', '0.0')

        success_msg = f"SUCCESS: Order ID {order_id} | Status: {status} | Executed Qty: {executed_qty} | Avg Price: {avg_price}"
        print(f"\n{success_msg}")
        logger.info(success_msg)

    except Exception as e:
        error_msg = f"FAILED: {str(e)}"
        print(f"\n{error_msg}")
        logger.error(error_msg)
        sys.exit(1)

if __name__ == "__main__":
    main()