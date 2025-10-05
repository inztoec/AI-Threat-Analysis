# AI-Powered Threat Profiler

This repository contains a series of Python scripts demonstrating an evolutionary approach to cybersecurity analytics. The project showcases how to advance from simple filtering to sophisticated, statistics-based threat profiling to detect covert Command and Control (C2) heartbeat traffic within simulated network data.

## Project Goal

The primary objective is to identify a stream of small, consistent malicious packets (a "heartbeat") hidden within a much larger volume of chaotic, benign network traffic. This project models a real-world cybersecurity challenge where anomaly detection must be intelligent enough to avoid being overwhelmed by false positives.

## The Scripts & Methodology

The detection model evolves across three distinct phases, each in its own script.

### 1. `threat_profiler.py` - Operation Alpha
*   **Methodology:** A naive, size-based filter. It identifies any packet smaller than a fixed threshold.
*   **Outcome:** Successfully identifies the anomalies in a simple environment but fails dramatically when "benign small packet" noise is introduced, leading to signal saturation and excessive false positives.

### 2. `threat_profiler_v2.py` - Operation Hydra
*   **Methodology:** Introduces a more realistic simulation containing three types of traffic: large normal traffic, small benign traffic (e.g., DNS, ACKs), and the small, consistent C2 threat.
*   **Outcome:** Demonstrates the failure of the V1 filter. It proves that simply filtering by size is insufficient in a noisy environment, as it flags hundreds of benign packets as threats.

### 3. `threat_profiler_v3.py` - Operation Watchtower
*   **Methodology:** The final, intelligent model. This script moves beyond individual packets to analyze "conversations" (traffic grouped by source/destination). It calculates the **standard deviation** and **mean** for each conversation.
*   **Threat Profile:** A connection is flagged as a threat if it meets two criteria:
    1.  **Low Mean Packet Size:** The conversation consists of small packets.
    2.  **Extremely Low Standard Deviation:** The packet sizes are highly consistent (a rhythmic pulse), unlike the chaotic nature of benign traffic.
*   **Outcome:** This behavioral profiling model successfully ignores the benign noise and accurately pinpoints the C2 connection, demonstrating a dramatic reduction in false positives and providing actionable intelligence.

## Technologies Used
*   **Language:** Python
*   **Libraries:** NumPy for numerical data manipulation and statistical analysis.
*   **Concepts:**
    *   Cybersecurity Threat Modeling
    *   Statistical Anomaly Detection
    *   Data Simulation & Modeling
    *   Algorithmic Design
    *   Behavioral Analysis vs. Signature-based Filtering

## How to Run

1.  Ensure you have Python and NumPy installed (`pip install numpy`).
2.  Clone this repository or download the scripts.
3.  Execute any of the scripts from your terminal:
    ```bash
    python3 threat_profiler_v3.py
    ```
