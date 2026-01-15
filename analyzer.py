import sys
import json
import os
import time
from scanner import scan_folder, get_context_with_metrics
from ai_engine import ask_llm
from experiment_tracker import log_experiment

def compare_approaches(approach_a_results, approach_b_results):
    """Compares two different scan settings to see which produced more data."""
    print("\n--- ⚖️ Comparison Results ---")
    diff = len(approach_b_results) - len(approach_a_results)
    if diff > 0:
        print(f"✅ Approach B found {diff} more relevant code blocks.")
    else:
        print(f"❌ Approach B did not improve coverage.")

def main():
    # 1. Start the timer at the very beginning of the script
    start_time = time.time() 
    
    # 2. Handle Arguments
    path_to_scan = "."
    user_query = None

    if len(sys.argv) > 1:
        if sys.argv[1] == "--ask":
            user_query = sys.argv[2] if len(sys.argv) > 2 else None
        else:
            path_to_scan = sys.argv[1]
            if "--ask" in sys.argv:
                ask_index = sys.argv.index("--ask")
                user_query = sys.argv[ask_index + 1] if len(sys.argv) > ask_index + 1 else None

    print(f"--- Scanning ERPNext Code at: {path_to_scan} ---")
    
    # 3. Perform the Scan (This is what we are measuring now)
    data = scan_folder(path_to_scan)
    
    # 4. Handle the Search and Latency Calculation
    if user_query:
        print(f"🔍 Searching for: '{user_query}'...")
        
        # Get context and precision from scanner
        relevant_context, precision = get_context_with_metrics(user_query, data)
        
        # Calculate Total Latency (Scanning + Searching)
        # Multiply by 1000 to get Milliseconds
        latency = (time.time() - start_time) * 1000 
        
        # Log the experiment
        log_experiment("exp-001", "Full System Latency", user_query, precision, latency)
        print(f"⏱️ Total Latency: {latency:.2f} ms")

    # 5. Save Summary Output
    if not os.path.exists("output"):
        os.makedirs("output")
    with open("output/summary.json", "w") as f:
        json.dump(data, f, indent=2)

    # 6. Print Final Summary
    print(f"\nFiles scanned  : {len(data)}")
    print(f"Functions found: {sum(len(f['functions']) for f in data)}")
    print("---------------------------------------")
    print("✅ Success! Check output/summary.json for details.")

if __name__ == "__main__":
    main()