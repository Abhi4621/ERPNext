import json
import os

def generate_trend_report():
    log_file = "output/experiments.jsonl"
    if not os.path.exists(log_file):
        print("No experiment data found to visualize.")
        return

    print(f"{'Date':<20} | {'Exp ID':<10} | {'Precision':<10} | {'Latency (ms)':<12}")
    print("-" * 60)

    with open(log_file, "r") as f:
        for line in f:
            data = json.loads(line)
            metrics = data['metrics']
            print(f"{data['date'][:19]:<20} | {data['exp_id']:<10} | {metrics['precision']:<10.2f} | {metrics['latency_ms']:<12.2f}")

generate_trend_report()