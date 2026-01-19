import streamlit as st
import time
import os
from scanner import scan_folder, get_context_with_metrics
from ai_engine import ask_llm
from experiment_tracker import log_experiment

st.set_page_config(page_title="ERPNext AI Code Assistant", layout="wide")

st.title("🤖 ERPNext AI Code Assistant")
st.markdown("### From CLI to UI: Bridging the gap to a VS Code Extension")

# Sidebar for Configuration
with st.sidebar:
    st.header("Settings")
    folder_path = st.text_input("Folder to Scan", value=".")
    if st.button("Re-scan Codebase"):
        with st.spinner("Scanning..."):
            st.session_state.data = scan_folder(folder_path)
            st.success(f"Scanned {len(st.session_state.data)} files!")

# Initialize data if not scanned
if 'data' not in st.session_state:
    st.session_state.data = scan_folder(folder_path)

# Main Chat Interface
query = st.text_input("Ask a question about your ERPNext code:")

if query:
    start_time = time.time()
    
    with st.spinner("Finding relevant code..."):
        # 1. Retrieval (The RAG Engine)
        relevant_context, precision = get_context_with_metrics(query, st.session_state.data)
        
        # 2. Measurement (Observability)
        latency = (time.time() - start_time) * 1000
        log_experiment("exp-UI-001", "Streamlit UI Test", query, precision, latency)
        
        # 3. Generation (AI Response)
        st.subheader("AI Analysis")
        answer = ask_llm(query, str(relevant_context))
        st.write(answer)
        
        # 4. Display Metrics to the User
        st.info(f"⏱️ Search Latency: {latency:.2f} ms | 🎯 Search Precision: {precision:.2%}")

    with st.expander("See Relevant Code Context"):
        st.json(relevant_context)