from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.circuit.library import GroverOperator
from qiskit.quantum_info import random_statevector
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import numpy as np

def teleportation_circuit_with_stabilizer(initial_state):
    qc = QuantumCircuit(5, 5)

    # Prepare initial state to be teleported
    qc.initialize(initial_state, 0)

    # Create Bell state between qubit 2 and 3
    qc.h(2)
    qc.cx(2, 3)

    # Apply gates for teleportation from qubit 0 to qubit 3
    qc.cx(0, 2)
    qc.h(0)

    # Measure qubits 0 and 2
    qc.measure([0, 2], [0, 2])

    # Apply stabilizer code for error correction
    qc.cx(2, 4)
    qc.cz(0, 4)

    # Apply conditional gates based on measurement results
    qc.cx(1, 3).c_if(qc.clbits[2], 1)
    qc.cz(0, 3).c_if(qc.clbits[0], 1)

    # Measure the final qubit 3
    qc.measure(3, 3)

    return qc

def run_teleportation_circuit_with_stabilizer(initial_state):
    qc = teleportation_circuit_with_stabilizer(initial_state)
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator, optimization_level=3)  # Уровень оптимизации

    result = simulator.run(compiled_circuit, shots=65536).result()  # Увеличиваем число выстрелов
    counts = result.get_counts()
    return counts

if __name__ == "__main__":
    # Initial state |+⟩
    initial_state_plus = [1/np.sqrt(2), 1/np.sqrt(2)]
    result_plus = run_teleportation_circuit_with_stabilizer(initial_state_plus)
    print("Quantum teleportation simulation result for state |+⟩ with stabilizer error correction:")
    print(result_plus)

    # Initial state |-⟩
    initial_state_minus = [1/np.sqrt(2), -1/np.sqrt(2)]
    result_minus = run_teleportation_circuit_with_stabilizer(initial_state_minus)
    print("Quantum teleportation simulation result for state |-⟩ with stabilizer error correction:")
    print(result_minus)
