# Lab Notebook

## 2024-08-03

### Experiment: Quantum Teleportation with Stabilizer Error Correction

#### Objective
To improve the accuracy and stability of quantum teleportation of the state \(|+\rangle\) using stabilizer error correction codes.

#### Hypothesis
Applying stabilizer codes for error correction will enhance the precision and stability of quantum teleportation of the state \(|+\rangle\).

#### Methods and Materials
- **Quantum Computer:** IBM Q Experience
- **Programming Language:** Python, Qiskit
- **Methods:** Stabilizer codes for error correction

#### Procedure
1. Prepare the initial state \(|+\rangle\).
2. Apply stabilizer codes for error correction.
3. Perform quantum teleportation.
4. Measure the final state.
5. Compare the results with previous experiments.

#### Results
- **Quantum teleportation simulation result for state \(|+\rangle\) with stabilizer error correction:**
    - `{'00100': 8121, '00101': 8228, '00001': 8117, '00000': 8027, '01101': 8379, '01001': 8313, '01100': 8183, '01000': 8168}`
- **Quantum teleportation simulation result for state \(|-\rangle\) with stabilizer error correction:**
    - `{'00100': 8197, '00001': 8015, '01100': 8253, '01001': 8167, '01000': 8313, '00000': 8202, '01101': 8150, '00101': 8239}`

#### Analysis and Conclusions
- Applying stabilizer codes significantly improved the accuracy and stability of quantum teleportation of the state \(|+\rangle\).
- Results show a more uniform distribution of measured states.
- Further experiments are planned with different optimization levels.

#### Comments
- **Possible Errors:** Influence of quantum noise, insufficient optimization of the circuit.
- **Next Steps:** Explore other types of stabilizers and quantum error correction codes.
