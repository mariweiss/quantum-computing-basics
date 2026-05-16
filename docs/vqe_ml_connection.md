# VQE and Machine Learning

## Variational Structure

The Variational Quantum Eigensolver (VQE) minimizes:

E(θ) = ⟨ψ(θ)| H |ψ(θ)⟩

Machine Learning minimizes:

L(θ) = Loss function

Both problems share the same structure:

θ* = argmin f(θ)

Where:
- θ are trainable parameters
- f(θ) is a cost function
- Optimization is classical

---

## Hybrid Optimization Loop

VQE uses:

1. Parameterized quantum circuit
2. Measurement of expectation value
3. Classical optimizer
4. Parameter update

This is structurally identical to training a neural network.

---

## Parametrized Quantum Circuits (PQC)

A PQC acts like a neural network:

Input → Quantum Gates → Measurement → Loss → Optimizer → Update θ

This framework is the basis of:

- Variational Quantum Classifiers
- Quantum Neural Networks
- Quantum Kernel Methods

VQE is therefore the foundation of Variational Quantum Machine Learning.