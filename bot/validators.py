def validate_order_input(symbol, side, order_type, quantity, price=None):
    """Basic validation for user inputs."""
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Invalid symbol. Example: BTCUSDT")
    
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be either BUY or SELL")
    
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be either MARKET or LIMIT")
    
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")
    
    if order_type.upper() == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("Price is required and must be greater than zero for LIMIT orders")
    
    return True