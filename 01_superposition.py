from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate
qc.h(0)

# Measure
qc.measure(0, 0)

# Simulator
simulator = Aer.get_backend('aer_simulator')
qc = transpile(qc, simulator)

result = simulator.run(qc, shots=1000).result()
counts = result.get_counts()

print(counts)
plot_histogram(counts)
plt.show()
