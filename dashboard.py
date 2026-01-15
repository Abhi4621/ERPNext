import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="ERPNext AI Experiment Tracker", layout="wide")
st.title("🧪 ERPNext AI Experiment Dashboard")

def load_data():
    data = []
    path = "output/experiments.jsonl"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        entry = json.loads(line)
                        flat_entry = {
                            "date": entry["date"],
                            "exp_id": entry["exp_id"],
                            "query": entry["query"],
                            "precision": entry["metrics"]["precision"],
                            "latency": entry["metrics"]["latency_ms"]
                        }
                        data.append(flat_entry)
                    except: continue
    return pd.DataFrame(data)

df = load_data()

if not df.empty:
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Precision", f"{df['precision'].mean():.2%}")
    col2.metric("Avg Latency", f"{df['latency'].mean():.0f} ms")
    col3.metric("Total Experiments", len(df))
    
    st.subheader("Precision Trend")
    st.line_chart(df.set_index('date')['precision'])
    
    st.subheader("Recent Logs")
    st.dataframe(df)
else:
    st.info("No data found in output/experiments.jsonl. Run your analyzer with --ask first!")
