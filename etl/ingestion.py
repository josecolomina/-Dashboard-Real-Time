import sqlite3
import time
import random
import datetime
import os

# Configuration
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'finance.db')
SYMBOLS = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'TSLA']

def init_db():
    """Initialize the database with the necessary table."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            price REAL NOT NULL,
            volume INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print(f"Database initialized at {DB_PATH}")

def generate_data():
    """Generate mock stock data."""
    symbol = random.choice(SYMBOLS)
    price = round(random.uniform(100, 2000), 2)
    volume = random.randint(100, 10000)
    return symbol, price, volume

def run_etl():
    """Continuous ETL process."""
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("Starting data ingestion... Press Ctrl+C to stop.")
    try:
        while True:
            symbol, price, volume = generate_data()
            timestamp = datetime.datetime.now().isoformat()
            
            cursor.execute('''
                INSERT INTO stock_prices (symbol, price, volume, timestamp)
                VALUES (?, ?, ?, ?)
            ''', (symbol, price, volume, timestamp))
            conn.commit()
            
            print(f"Ingested: {symbol} | ${price} | Vol: {volume} | {timestamp}")
            time.sleep(1) # Simulate real-time data every second
    except KeyboardInterrupt:
        print("\nStopping data ingestion.")
    finally:
        conn.close()

if __name__ == "__main__":
    run_etl()
