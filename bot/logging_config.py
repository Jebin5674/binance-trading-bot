import logging

def setup_logging():
    # This creates a log file named 'bot_activity.log'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("bot_activity.log"), # Writes to file
            logging.StreamHandler()                 # Also prints to console
        ]
    )
    return logging.getLogger("TradingBot")