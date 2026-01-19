import streamlit as st
import pandas as pd
import json
import os

# Set page layout
st.set_page_config(page_title="ERPNext AI Experiment Tracker", layout="wide")
st.title("🧪 ERPNext AI Experiment Dashboard")

def load_data():
    data = []
    path = "output/experiments.jsonl"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                    # Use .get() to avoid errors if a key is missing
                    metrics = entry.get("metrics", {})
                    flat_entry = {
                        "date": entry.get("date", "N/A"),
                        "exp_id": entry.get("exp_id", "N/A"),
                        "query": entry.get("query", "N/A"),
                        "precision": metrics.get("precision", 0),
                        "latency": metrics.get("latency_ms", 0)
                    }
                    data.append(flat_entry)
                except Exception:
                    continue
    return pd.DataFrame(data)

df = load_data()

if not df.empty:
    # 1. Dashboard Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Precision", f"{df['precision'].mean():.2%}")
    col2.metric("Avg Latency", f"{df['latency'].mean():.0f} ms")
    col3.metric("Total Experiments", len(df))
    
    # 2. Precision Trend Chart
    st.subheader("Precision Trend")
    st.line_chart(df.set_index('date')['precision'])
    
    # 3. Data Table
    st.subheader("Recent Logs")
    st.dataframe(df)
else:
    st.info("No data found in output/experiments.jsonl. Run your analyzer with --ask first!")