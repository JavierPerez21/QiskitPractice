from random-circuit-generator import *

# Generate a random circuit
circuit = RandomCircuitGenerator(qubits=1, max_depth=2)
circuit.generate_random_circuit()

# Visualize som information about the random circuit
#circuit.execution_historgram()
circuit.bloch_sphere()
circuit.q_sphere()
#circuit.show_circuit()

# Try to generate  a similar circuit
circuit_guess = QuantumCircuit(1)
circuit_guess.h(0)
circuit.add_circuit_guess(circuit_guess)