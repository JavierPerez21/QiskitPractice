from qiskit import *
import numpy as np
from math import pi
from qiskit.visualization import plot_histogram, plot_bloch_multivector, plot_state_qsphere, plot_state_city
from qiskit.quantum_info import Statevector
from qiskit.quantum_info import state_fidelity
import matplotlib.pyplot as plt


class RandomCircuitGenerator:
    def __init__(self, qubits=1, max_depth=3):
        self.qubits = np.arange(0,qubits).tolist()
        self.max_depth = max_depth
        self.qc = QuantumCircuit(qubits, qubits)
        self.single_qubit_gates = ['x', 'z', 'y', 'h', 's', 't', 'rx', 'rz', 'ry', '']
        self.multi_qubit_gates = ['cx', 'cz', 'cy', 'ch', 'cs', 'ct', 'crx', 'crz', 'cry', '']
        self.angles = [0, pi / 8, pi / 4, 3 * pi / 8, pi / 2, 5 * pi / 8, 3 * pi / 4, 7 * pi / 8, pi, 9 * pi / 8,
                       5 * pi / 4, 11 * pi / 8, 3 * pi / 2, 13 * pi / 8, 7 * pi / 4, 15 * pi / 8, 2 * pi]
        if len(self.qubits) > 1:
            self.available_gates = self.single_qubit_gates + self.multi_qubit_gates
        else:
            self.available_gates = self.single_qubit_gates

    def generate_random_circuit(self):
        for i in range(0, self.max_depth):
            gate = self.available_gates[np.random.randint(0, len(self.available_gates))]
            self.add_gate(gate)

    def add_gate(self, gate):
        if gate == 'x':
            qubit = self.qubits[np.random.randint(0, len(self.qubits))]
            self.qc.x(qubit)
        elif gate == 'z':
            qubit = self.qubits[np.random.randint(0, len(self.qubits))]
            self.qc.z(qubit)
        elif gate == 'y':
            qubit = self.qubits[np.random.randint(0, len(self.qubits))]
            self.qc.y(qubit)
        elif gate == 'h':
            qubit = self.qubits[np.random.randint(0, len(self.qubits))]
            self.qc.h(qubit)
        elif gate == 's':
            qubit = self.qubits[np.random.randint(0, len(self.qubits))]
            self.qc.s(qubit)
        elif gate == 't':
            qubit = self.qubits[np.random.randint(0, len(self.qubits))]
            self.qc.t(qubit)
        elif gate == 'rx':
            qubit = self.qubits[np.random.randint(0, len(self.qubits))]
            angle = self.angles[np.random.randint(0, len(self.angles))]
            self.qc.rx(angle, qubit)
        elif gate == 'rz':
            qubit = self.qubits[np.random.randint(0, len(self.qubits))]
            angle = self.angles[np.random.randint(0, len(self.angles))]
            self.qc.rz(angle, qubit)
        elif gate == 'ry':
            qubit = self.qubits[np.random.randint(0, len(self.qubits))]
            angle = self.angles[np.random.randint(0, len(self.angles))]
            self.qc.ry(angle, qubit)
        elif gate == 'cx':
            qubit1 = self.qubits[np.random.randint(0, len(self.qubits))]
            qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            while qubit1 == qubit2:
                qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            self.qc.cx(qubit1, qubit2)
        elif gate == 'cz':
            qubit1 = self.qubits[np.random.randint(0, len(self.qubits))]
            qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            while qubit1 == qubit2:
                qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            self.qc.cz(qubit1, qubit2)
        elif gate == 'cy':
            qubit1 = self.qubits[np.random.randint(0, len(self.qubits))]
            qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            while qubit1 == qubit2:
                qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            self.qc.cy(qubit1, qubit2)
        elif gate == 'ch':
            qubit1 = self.qubits[np.random.randint(0, len(self.qubits))]
            qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            while qubit1 == qubit2:
                qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            self.qc.ch(qubit1, qubit2)
        elif gate == 'cs':
            qubit1 = self.qubits[np.random.randint(0, len(self.qubits))]
            qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            while qubit1 == qubit2:
                qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            self.qc.cs(qubit1, qubit2)
        elif gate == 'ct':
            qubit1 = self.qubits[np.random.randint(0, len(self.qubits))]
            qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            while qubit1 == qubit2:
                qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            self.qc.ct(qubit1, qubit2)
        elif gate == 'crx':
            qubit1 = self.qubits[np.random.randint(0, len(self.qubits))]
            qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            while qubit1 == qubit2:
                qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            angle = self.angles[np.random.randint(0, len(self.angles))]
            self.qc.crx(angle, qubit1, qubit2)
        elif gate == 'crz':
            qubit1 = self.qubits[np.random.randint(0, len(self.qubits))]
            qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            while qubit1 == qubit2:
                qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            angle = self.angles[np.random.randint(0, len(self.angles))]
            self.qc.crz(angle, qubit1, qubit2)
        elif gate == 'cry':
            qubit1 = self.qubits[np.random.randint(0, len(self.qubits))]
            qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            while qubit1 == qubit2:
                qubit2 = self.qubits[np.random.randint(0, len(self.qubits))]
            angle = self.angles[np.random.randint(0, len(self.angles))]
            self.qc.cry(angle, qubit1, qubit2)

    def show_circuit(self):
        print(self.qc)

    def execution_historgram(self):
        qc = self.qc.copy()
        qc.measure(self.qubits, self.qubits)
        backend = BasicAer.get_backend('qasm_simulator')
        job = execute(qc, backend)
        plot_histogram(job.result().get_counts(), color='midnightblue', title="Execution Histogram")
        plt.show()

    def bloch_sphere(self):
        qc = self.qc.copy()
        state = Statevector.from_instruction(qc)
        plot_bloch_multivector(state, title="Bloch Sphere", reverse_bits=False)
        plt.show()

    def q_sphere(self):
        qc = self.qc.copy()
        state = Statevector.from_instruction(qc)
        plot_state_qsphere(state)
        plt.show()

    def state_city(self):
        qc = self.qc.copy()
        backend = BasicAer.get_backend('statevector_simulator')
        result = backend.run(transpile(qc, backend)).result()
        psi = result.get_statevector(qc)
        plot_state_city(psi)
        plt.show()

    def add_circuit_guess(self, circuit_guess):
        qc = self.qc.copy()
        self.circuit_guess = circuit_guess
        circuit_guess = circuit_guess.copy()

        backend = BasicAer.get_backend('statevector_simulator')
        qc_state = execute(qc, backend).result().get_statevector(qc)
        circuit_guess_state = execute(circuit_guess, backend).result().get_statevector(circuit_guess)
        print("State fidelity of your circuit: {}".format(state_fidelity(circuit_guess_state, qc_state)))

