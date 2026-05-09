# Binance Futures Trading Bot (USDT-M)

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Binance](https://img.shields.io/badge/Binance-Testnet-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

A modular, robust Python application designed to execute Market and Limit orders on the Binance Futures Testnet. This project demonstrates clean architecture, strict input validation, and comprehensive logging for high-frequency trading environments.

## 🚀 Key Features

- **Multi-Order Support**: Seamlessly place both `MARKET` and `LIMIT` orders.
- **Robust Validation**: Pre-execution checks for symbols, quantities, and notional values to prevent API waste.
- **Structured Architecture**: Clear separation between the API client layer, business logic, and CLI interface.
- **Advanced Logging**: Automated logging of all API requests, successful responses, and error stack traces to `bot_activity.log`.
- **Error Resilience**: Graceful handling of network failures, insufficient margin, and API-specific exceptions.

## 🛠 Tech Stack

- **Language**: Python 3.x
- **API Wrapper**: `python-binance`
- **Environment Management**: `python-dotenv`
- **Logging**: Python Native Logging Module

## 📁 Project Structure

```text
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py        # Binance API initialization
│   ├── orders.py        # Order execution logic
│   ├── validators.py    # Input and business logic validation
│   └── logging_config.py# Centralized logging configuration
├── cli.py               # Main entry point (Command Line Interface)
├── .env                 # API Credentials (Hidden)
├── bot_activity.log     # Generated activity logs
└── requirements.txt     # Project dependencies
⚙️ Setup & Installation
Clone the repository:
code
Bash
git clone https://github.com/YOUR_USERNAME/binance-trading-bot.git
cd binance-trading-bot
Create Virtual Environment:
code
Bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install Dependencies:
code
Bash
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the root directory:
code
Text
BINANCE_API_KEY=your_testnet_key
BINANCE_API_SECRET=your_testnet_secret
💻 Usage Examples
Place a Market Order
code
Bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
Place a Limit Order
code
Bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 55000
📝 Assumptions
Minimum Notional: Orders must meet the Binance minimum notional value (usually > 50 USDT).
Testnet: The bot is hardcoded to use the Binance Futures Testnet environment for safety.
Developed as part of the Primetrade.ai Application Task.
code
Code
---

### 2. How to show the "Small Explanation" (The "About" Section)
In your third image, some projects show a summary on the right side under "About." To do this:

1. Go to your repository page on GitHub.
2. On the right-hand side, find the **About** section.
3. Click the **Gear icon (⚙️)**.
4. In the **Description** box, type: 
   > *A Python-based trading bot for Binance Futures Testnet with modular architecture, logging, and error handling.*
5. Add some tags like `python`, `binance-api`, `trading-bot`.
6. Click **Save changes**.

---

### 3. Final Step: The Folder View
To make the folder view look like your first image:
*   Make sure you have a file named `.gitignore` in your root folder so that the `venv/` folder is **not** uploaded.
*   The folder structure I provided in the README's `Project Structure` section uses a "Tree" format which looks very professional to recruiters.

### Summary of Files to upload to GitHub:
1. `bot/` (folder with all 5 files)
2. `cli.py`
3. `requirements.txt`
4. `README.md`
5. `.gitignore`
6. `bot_activity.log` (Upload this so they can see your successful runs!)