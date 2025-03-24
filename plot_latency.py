import os
import pandas as pd
import matplotlib.pyplot as plt

log_file = "logs/latency_log.csv"
output_file = "logs/latency_plot.png"

if not os.path.exists(log_file):
    print(f"❌ CSV not found: {log_file}")
    exit(0)  # Prevents workflow from failing

df = pd.read_csv(log_file)
df["relative_time"] = df["measurement_time"] - df["measurement_time"].min()

plt.figure(figsize=(10, 5))
plt.plot(df["relative_time"], df["latency_ms"], marker='o', linestyle='-', label="Latency (ms)")
plt.xlabel("Time (s)")
plt.ylabel("Latency (ms)")
plt.title("Video Stream Latency Over Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(output_file)
plt.close()
