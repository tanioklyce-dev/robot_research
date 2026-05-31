# cubff — paradigms-of-intelligence/cubff (GitHub README capture)

> Raw capture (markdown extraction via WebFetch) of https://github.com/paradigms-of-intelligence/cubff
> Fetched 2026-05-31. Maintainer: Google Paradigms of Intelligence Team. License: Apache-2.0.

## What is cubff?
"A (optionally) CUDA-based implementation of a self-modifying soup of programs which
show emergence of self-replicators."

## Research Foundation
Supports the experiments in "Computational Life: How Well-formed, Self-replicating
Programs Emerge from Simple Interaction" (https://arxiv.org/abs/2406.19108). Most
experiments from the paper were run with this implementation.

## Supported Languages / Substrates
- BFF (Brainfuck variants: `bff_noheads`, `bff8`, `bff_perm`, `bff_selfmove`)
- Forth implementations
- SUBLEQ (subtract and branch if less than or equal)
- RSUBLEQ4 (reverse SUBLEQ)

## Build Requirements
- Debian/Ubuntu: `build-essential`, `libbrotli-dev`
- Arch Linux: `base-devel`, `brotli`
- Optional: CUDA support

## Build Instructions
- CUDA-enabled: `make`
- CPU-only: `make CUDA=0`

## Usage Example
`bin/main --lang bff_noheads`

Python bindings available via `cubff.py`.

## Repository Metrics (at capture)
- License: Apache-2.0
- Stars: 200 / Forks: 48
- Language composition: C++ (38.9%), Python (25.5%), HTML (17.8%), CUDA (16.2%)
- Includes test data and GitHub Actions CI/CD workflows.
