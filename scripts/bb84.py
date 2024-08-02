from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import random

def bb84_sender():
    qc = QuantumCircuit(1, 1)
    bit = random.randint(0, 1)
    basis = random.choice(['X', 'Z'])

    if basis == 'X':
        qc.h(0)
    if bit == 1:
        qc.x(0)

    qc.measure(0, 0)
    return qc, basis, bit

def bb84_receiver(qc, basis):
    if basis == 'X':
        qc.h(0)
    qc.measure(0, 0)
    return qc

def run_bb84():
    sender_circuit, sender_basis, sender_bit = bb84_sender()
    receiver_basis = random.choice(['X', 'Z'])
    receiver_circuit = bb84_receiver(sender_circuit, receiver_basis)

    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(receiver_circuit, simulator, optimization_level=3)  # Уровень оптимизации
    result = simulator.run(compiled_circuit).result()
    counts = result.get_counts()

    return sender_bit, sender_basis, receiver_basis, counts

if __name__ == "__main__":
    sender_bit, sender_basis, receiver_basis, result = run_bb84()
    print(f"Sender bit: {sender_bit}")
    print(f"Sender basis: {sender_basis}")
    print(f"Receiver basis: {receiver_basis}")
    print(f"Measurement result: {result}")
