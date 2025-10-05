# threat_profiler_v2.py

import numpy as np

# --- SIMULATION DATA ---

# 1. Normal Traffic (High volume, high variability)
# Represents users watching videos, browsing, etc.
normal_traffic = np.random.randint(500, 4500, 800)

# 2. The REAL Threat: C2 Heartbeats (Low volume, very low variability)
# The malware "phoning home".
c2_heartbeats = np.random.randint(60, 75, 20)

# 3. The FALSE Alarms: Benign Small Packets (Medium volume, medium variability)
# Represents DNS lookups, TCP ACKs, Pings, etc.
benign_small_packets = np.random.randint(40, 120, 150)


# --- COMBINE AND SHUFFLE ---

# Combine all three types of traffic into a single array
all_traffic = np.concatenate([normal_traffic, c2_heartbeats, benign_small_packets])

# Shuffle the array to simulate the randomness of a real network feed
np.random.shuffle(all_traffic)


# --- ANALYSIS ---

# 1. Run the old, simple filter: Is the packet size small?
heartbeat_candidates = all_traffic[all_traffic < 150] # Using 150 to be safe

# 2. Report the findings
print(f"OPERATION HYDRA REPORT")
print(f"----------------------")
print(f"Initial filter (< 150 bytes) flagged {len(heartbeat_candidates)} packets as potential threats.")
print(f"This is too many for a human analyst to investigate manually.")
print(f"Here are the first 50 candidates found: \n{heartbeat_candidates[:50]}")