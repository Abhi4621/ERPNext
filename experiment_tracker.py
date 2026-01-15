import json
import datetime
import os

def log_experiment(exp_id, hypothesis, query, precision, latency):
    """Tracks experiments to understand what improves context quality."""
    log_entry = {
        "date": str(datetime.datetime.now()),
        "exp_id": exp_id,
        "hypothesis": hypothesis,
        "query": query,
        "metrics": {
            "precision": round(precision, 4), # Context Precision metric
            "latency_ms": round(latency, 2)   # Latency metric
        }
    }
    
    if not os.path.exists("output"):
        os.makedirs("output")
        
    log_file = "output/experiments.jsonl" # Simple JSON Lines tracking
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")
    
    print(f"🧪 Experiment {exp_id} logged to {log_file}")