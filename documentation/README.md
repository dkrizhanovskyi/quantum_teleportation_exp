# Quantum Networks Project

## Overview

This project focuses on quantum teleportation and error correction methods. The goal is to improve the accuracy and stability of quantum teleportation using different error correction techniques, including stabilizer codes.

## Project Structure

- `data/`: Contains raw, processed, and result data from experiments.
- `scripts/`: Python scripts for running experiments and analyzing results.
    - `bb84.py`: Script for the BB84 quantum key distribution protocol.
    - `teleportation.py`: Basic quantum teleportation script.
    - `teleportation_with_error_correction.py`: Quantum teleportation with basic error correction.
    - `teleportation_with_stabilizer_error_correction.py`: Quantum teleportation with stabilizer error correction.
    - `analysis.py`: Script for analyzing and visualizing experimental results.
- `documentation/`: Documentation of the project, including the lab notebook and readme.
    - `lab_notebook.md`: Detailed log of experiments and results.
    - `readme.md`: Overview of the project.
- `reports/`: Reports generated from experiments and analyses.
    - `experiment_results_2024-08-03.pdf`: Detailed results of experiments conducted on August 3, 2024.
    - `analysis_report_2024-08-03.pdf`: Analysis report of the results obtained on August 3, 2024.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/quantum_networks.git
    cd quantum_networks
    ```

2. Install the required Python packages:
    ```bash
    pip install qiskit qiskit-aer matplotlib numpy pandas
    ```

## Usage

### Running Experiments

- **BB84 Protocol**:
    ```bash
    python scripts/bb84.py
    ```

- **Basic Quantum Teleportation**:
    ```bash
    python scripts/teleportation.py
    ```

- **Quantum Teleportation with Error Correction**:
    ```bash
    python scripts/teleportation_with_error_correction.py
    ```

- **Quantum Teleportation with Stabilizer Error Correction**:
    ```bash
    python scripts/teleportation_with_stabilizer_error_correction.py
    ```

### Analyzing Results

- To analyze and visualize the results:
    ```bash
    python scripts/analysis.py
    ```

## Documentation

For detailed logs of the experiments and results, please refer to `documentation/lab_notebook.md`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
