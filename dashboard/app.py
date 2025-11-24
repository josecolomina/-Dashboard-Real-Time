import streamlit as st
import pandas as pd
import sqlite3
import time
import plotly.express as px
import os

# Configuration
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'finance.db')

st.set_page_config(
    page_title="Real-Time Financial Dashboard",
    page_icon="📈",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

def get_data():
    """Fetch the latest data from the database."""
    if not os.path.exists(DB_PATH):
        return pd.DataFrame()
    
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT * FROM stock_prices ORDER BY timestamp DESC LIMIT 1000"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def main():
    st.title("📈 Real-Time Financial Dashboard")
    st.markdown("### Live Market Data Feed")

    # Placeholder for real-time updates
    placeholder = st.empty()

    while True:
        df = get_data()
        
        if df.empty:
            placeholder.warning("Waiting for data ingestion... Please run `python etl/ingestion.py`")
            time.sleep(2)
            continue

        df['timestamp'] = pd.to_datetime(df['timestamp'])
        latest_data = df.groupby('symbol').first().reset_index()

        with placeholder.container():
            # KPIs
            kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
            
            # Display metrics for up to 5 symbols
            cols = [kpi1, kpi2, kpi3, kpi4, kpi5]
            for i, row in enumerate(latest_data.itertuples()):
                if i < 5:
                    cols[i].metric(
                        label=row.symbol,
                        value=f"${row.price:,.2f}",
                        delta=f"Vol: {row.volume}"
                    )

            # Charts
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Price Trends (Last 1000 ticks)")
                fig_price = px.line(df, x='timestamp', y='price', color='symbol', title='Stock Prices Over Time')
                st.plotly_chart(fig_price, use_container_width=True)

            with col2:
                st.subheader("Volume Analysis")
                fig_vol = px.bar(latest_data, x='symbol', y='volume', title='Latest Trade Volume by Symbol')
                st.plotly_chart(fig_vol, use_container_width=True)

            # Recent Data Table
            st.subheader("Recent Transactions")
            st.dataframe(df.head(10), use_container_width=True)
            
            time.sleep(1) # Refresh every second

if __name__ == "__main__":
    main()
