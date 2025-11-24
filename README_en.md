# 📈 Real-Time Financial Dashboard

This project is an **interactive dashboard** designed to visualize financial metrics in real-time. It simulates continuous market data ingestion (stock prices, volume) and presents them in a dynamic and modern dashboard.

The main goal is to demonstrate the implementation of a complete data architecture, from data generation and storage to live visualization.

## 🚀 Key Features

*   **Real-Time Data Ingestion (ETL)**: A Python script (`etl/ingestion.py`) generates mock market data and continuously loads it into a database.
*   **Persistent Storage**: Uses **SQLite** to store transaction history, enabling historical analysis and data persistence.
*   **Interactive Visualization**: Dashboard built with **Streamlit** that automatically updates to show the latest market movements.
*   **Key Metrics**: Visualization of instant KPIs, line charts for price trends, and bar charts for volume analysis.

## 🛠️ Technologies Used

*   **Python**: Core language of the project.
*   **Streamlit**: Framework for creating the interactive web dashboard.
*   **SQLite**: Lightweight and efficient SQL database for data storage.
*   **Pandas**: Data manipulation and analysis.
*   **Plotly**: Interactive graphing library for visualizations.

## 📂 Project Structure

```
Dashboard-Real-Time/
├── dashboard/
│   └── app.py            # Main Streamlit Application (Frontend)
├── data/
│   └── finance.db        # SQLite Database (automatically generated)
├── etl/
│   └── ingestion.py      # Data Ingestion Script (ETL Backend)
├── requirements.txt      # Project Dependencies
├── README.md             # Documentation in Spanish
└── README_en.md          # Documentation in English
```

## ⚙️ Installation and Usage

Follow these steps to run the project on your local machine:

1.  **Clone the repository**:
    ```bash
    git clone <REPOSITORY_URL>
    cd Dashboard-Real-Time
    ```

2.  **Install dependencies**:
    Ensure you have Python installed. Using a virtual environment is recommended.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Start the Data Ingestion Process (ETL)**:
    Open a terminal and run the ingestion script. This script must keep running to simulate the real-time data flow.
    ```bash
    python etl/ingestion.py
    ```
    *You will see logs in the console indicating data is being inserted.*

4.  **Launch the Dashboard**:
    Open a **second terminal** and run the Streamlit application.
    ```bash
    streamlit run dashboard/app.py
    ```

5.  **Explore**:
    The dashboard will automatically open in your browser (usually at `http://localhost:8501`). You will see charts and metrics updating in real-time as the ETL script inserts new data.

## 🔍 How It Works

1.  **Generation**: `etl/ingestion.py` creates random stock records (Symbol, Price, Volume) every second.
2.  **Storage**: These records are saved into the `stock_prices` table within `data/finance.db`.
3.  **Reading**: `dashboard/app.py` queries the database periodically to fetch the latest 1000 records.
4.  **Visualization**: Streamlit processes the data with Pandas and updates the Plotly charts and metrics in the user interface.

---
*This project is part of my professional portfolio, demonstrating skills in Data Engineering and Full Stack Development with Python.*
