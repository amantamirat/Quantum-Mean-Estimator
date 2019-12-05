'''
Created on Nov 14, 2019

@author: amanuel
'''
from math import log2, sqrt, pi
from qiskit import (QuantumRegister, ClassicalRegister, QuantumCircuit, BasicAer, execute, IBMQ)
from MyGates import n_controlled_x
from QRAM import load
from MyUtil import calc_mean, toVectors


def quantum_mean(v):
    
    IBMQ.load_account()
    provider = IBMQ.get_provider(group='open')
    # backend = provider.get_backend('ibmq_16_melbourne')
    # backend = provider.get_backend('ibmq_essex')
    # backend = provider.get_backend('ibmq_london')
    backend = provider.get_backend('ibmq_qasm_simulator')    
    # backend = BasicAer.get_backend('qasm_simulator')
    
    n = int(log2(len(v)))
    d = len(v[0])
    a = QuantumRegister(1)
    qr0 = QuantumRegister(n)
    qr1 = QuantumRegister(d + 1)
    qr2 = QuantumRegister(d + 1)  
    cr = ClassicalRegister(d + 1)
    circuit = QuantumCircuit(a, qr0, qr1, qr2, cr, name="quantum_mean")
    
    circuit.h(qr0)
    load(circuit, qr0, [qr1[i] for i in range(d)], v)
    circuit.x(qr1[d])
    
    circuit.h(qr0)
    circuit.x(qr0)
    n_controlled_x(circuit, qr0, a[0])
    for i in range(d + 1):
        circuit.ccx(a[0], qr1[i], qr2[i])
    n_controlled_x(circuit, qr0, a[0])
    circuit.x(qr0)
    circuit.h(qr0)
    
    circuit.measure(qr2, cr)
    result = execute(circuit, backend, shots=8192).result()
    
    counts = result.get_counts(circuit)
    print(counts)
    
    mean = [0] * int(pow(2, d + 1))
    for c in counts:
        print("prob of ", c, counts[c] / 8192)
        mean[int(c, 2)] = sqrt(counts[c] / 8192)
    return mean



v = [[1.965587446494658, pi / 2],
[1.0808390005411688, 0.9272952180016123],
[pi / 2, pi],
[1.21108932720994, 2.3005239830218627],
[2.0849933355795707, -1.0471975511965979],
[1.1616780010823367, 4.7243401093344528],
[pi / 2, pi / 16],
[1.2293259038443314, 1.6435011087932846],
[1.965587446494658, 1.0808390005411688],
[1.21108932720994, 3.0849933355795707],
[pi / 8, pi / 4],
[0.5547001962252291, 0.8320502943378437],
[0.4472135954999579, 0.8944271909999159],
[0.7808688094430304, 0.6246950475544243],
[0.39391929857916763, 0.9191450300180578],
[pi / 64, pi / 128]]


V = toVectors(v)
print("input vectors")
print(V)
print("classical mean:", calc_mean(V))
print("quantum mean: ", quantum_mean(v))

