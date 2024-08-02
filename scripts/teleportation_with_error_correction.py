from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.transpiler import PassManager, passes
import numpy as np

def teleportation_circuit_with_error_correction(initial_state):
    qc = QuantumCircuit(3, 3)

    # Prepare initial state to be teleported
    qc.initialize(initial_state, 0)

    # Create Bell state between qubit 1 and 2
    qc.h(1)
    qc.cx(1, 2)

    # Apply gates for teleportation from qubit 0 to qubit 2
    qc.cx(0, 1)
    qc.h(0)

    # Measure qubits 0 and 1
    qc.measure([0, 1], [0, 1])

    # Apply conditional gates based on measurement results
    qc.cx(1, 2).c_if(qc.clbits[1], 1)
    qc.cz(0, 2).c_if(qc.clbits[0], 1)

    # Measure the final qubit 2
    qc.measure(2, 2)

    return qc

def run_teleportation_circuit_with_error_correction(initial_state):
    qc = teleportation_circuit_with_error_correction(initial_state)
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator, optimization_level=3)  # Уровень оптимизации

    # Add error correction
    pm = PassManager(passes.RemoveResetInZeroState())
    compiled_circuit = pm.run(compiled_circuit)

    result = simulator.run(compiled_circuit, shots=65536).result()  # Увеличиваем число выстрелов
    counts = result.get_counts()
    return counts

if __name__ == "__main__":
    # Initial state |+⟩
    initial_state_plus = [1/np.sqrt(2), 1/np.sqrt(2)]
    result_plus = run_teleportation_circuit_with_error_correction(initial_state_plus)
    print("Quantum teleportation simulation result for state |+⟩ with error correction:")
    print(result_plus)

    # Initial state |-⟩
    initial_state_minus = [1/np.sqrt(2), -1/np.sqrt(2)]
    result_minus = run_teleportation_circuit_with_error_correction(initial_state_minus)
    print("Quantum teleportation simulation result for state |-⟩ with error correction:")
    print(result_minus)
