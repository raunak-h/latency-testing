import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

# Load CSV
df = pd.read_csv("logs/latency_log.csv")

# Convert absolute measurement time to relative time (in seconds)
df["relative_time"] = df["measurement_time"] - df["measurement_time"].min()

# Plot
plt.figure(figsize=(10, 5))
plt.plot(df["relative_time"], df["latency_ms"], marker='o', linestyle='-', label="Latency (ms)")
plt.xlabel("Time (s)")
plt.ylabel("Latency (ms)")
plt.title("Video Stream Latency Over Time")
plt.grid(True)
plt.legend()

# Save to file
plt.tight_layout()
plt.savefig("logs/latency_plot.png")
plt.close()
