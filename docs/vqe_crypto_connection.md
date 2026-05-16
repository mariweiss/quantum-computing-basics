# VQE and Cryptography

## Optimization Problems in Cryptography

Modern cryptography relies on hard mathematical problems:

- Integer factorization (RSA)
- Discrete logarithm (ECC)
- Lattice problems (Post-Quantum Cryptography)

These can often be reformulated as optimization problems.

---

## Variational Algorithms and Search

VQE demonstrates a general hybrid optimization paradigm:

θ* = argmin ⟨ψ(θ)| H |ψ(θ)⟩

This structure can be adapted to:

- QUBO problems
- SAT problems
- Combinatorial optimization

Many cryptographic attacks can be mapped to search or optimization problems.

---

## Relevance

While Shor’s algorithm directly breaks RSA via period finding,
variational quantum algorithms explore a different paradigm:

Quantum-assisted optimization.

Understanding VQE helps understand:

- Quantum complexity
- Hybrid quantum-classical attacks
- Limits of near-term quantum devices