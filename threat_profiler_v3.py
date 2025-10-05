import numpy as np
import random
MY_PC = '192.168.1.101'
GOOGLE_DNS = '8.8.8.8'
GAME_SERVER = '204.79.197.200'
SUSPICIOUS_SERVER = '151.101.65.195' # A seemingly random IP

NORMAL_DESTINATIONS = [GOOGLE_DNS, GAME_SERVER, '104.16.248.249', '99.84.219.82']
traffic_log = {}
for _ in range(800):
    destination = random.choice(NORMAL_DESTINATIONS)
    connection = (MY_PC, destination)
    packet_size = np.random.randint(300, 4500)
    traffic_log.setdefault(connection, []).append(packet_size)
connection_dns = (MY_PC, GOOGLE_DNS)
for _ in range(150):
    packet_size = np.random.randint(40, 120)
    traffic_log.setdefault(connection_dns, []).append(packet_size)
connection_c2 = (MY_PC, SUSPICIOUS_SERVER)
for _ in range(25): # A small number of packets
    packet_size = np.random.randint(60, 75) # Very tight, consistent size
    traffic_log.setdefault(connection_c2, []).append(packet_size)

print("--- Data simulation complete. Traffic log contains", len(traffic_log), "unique connections. ---")
print("\nScanning connections for suspicious patterns...")

for connection, packet_sizes in traffic_log.items():
    # We need enough data to make a reliable judgement
    if len(packet_sizes) < 15:
        continue # Not enough traffic, skip to the next one

    # Calculate key statistical properties for this specific connection
    std_dev = np.std(packet_sizes)
    mean_size = np.mean(packet_sizes)
    num_packets = len(packet_sizes)
    
    # --- The Core Logic: Define the Threat Profile ---
    # A threat is a stream of packets that is:
    # 1. Very CONSISTENT (Extremely low standard deviation)
    # 2. Made of SMALL packets (Low mean size)
    
    is_consistent = std_dev < 5.0
    is_small = mean_size < 100.0

    # Report our findings
    print(f"\n--- Connection: {connection[0]} -> {connection[1]} ---")
    print(f"    Packets: {num_packets} | Avg Size: {mean_size:.2f} | Std Dev: {std_dev:.2f}")

    if is_consistent and is_small:
        print("    >>>>> THREAT DETECTED: This connection matches the C2 Heartbeat profile! <<<<<")
                