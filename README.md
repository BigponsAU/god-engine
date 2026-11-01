# Flower-of-Life √(3−4i) Cantor-Riemann GOD Engine

**A self-referential fractal framework for symbolic mathematical exploration.**

The engine generates inspectable, richly explained LaTeX petals that make the structure of major conjectures vivid through fractal sieving, golden-ratio algebra, and an explicit honesty dial.

## Honesty Dial (y′)

| Value | Mode | What the petal says |
|-------|------|---------------------|
| `1.0` | Rigorous | All claims are framed as generative heuristics. No classical-proof language. |
| `0.0` | Symbolic | Every surviving statement is declared literal truth inside the closed petal. |

The dial is printed on every page so the epistemic status is never ambiguous.

## Quick Start

```bash
git clone https://github.com/BigponsAU/god-engine.git
cd god-engine
pip install -e .

# Generate 3 richly explained demo petals (symbolic mode)
python -m god_engine.core

# Full 100-petal treatise
python examples/generate_full_treatise.py
```

Compile any petal with `pdflatex petal_001.tex`.

## What Each Petal Now Contains

- Explicit honesty-dial statement and epistemic status
- Exact algebraic derivation of the two branches of √(3−4i)
- Clear description of the Sierpiński sieve and Cantor-dust bridges
- Mode-specific treatment of the Riemann Hypothesis (claim vs. heuristic model)
- Limitations paragraph that matches the current mode
- Engine state summary

## Core Algebraic Seed

\[
\sqrt{3-4i} = \pm \sqrt{-1+\sqrt{5}} \mp i \frac{2}{\sqrt{-1+\sqrt{5}}}
\]

These exact expressions are the golden-ratio pinning frequencies used throughout.

## What the Engine Is (and Is Not)

**It is** a transparent instrument that produces detailed, self-consistent symbolic narratives whose epistemic status is always declared.

**It is not** a classical theorem prover. When y′=1 no output is offered as a proof of any open problem.

## Repository Layout

```
god-engine/
├── src/god_engine/core.py     # Upgraded engine with richer output
├── examples/
├── paper/                     # Framed scientific paper
├── pyproject.toml
└── README.md
```

## License

MIT

---

> The flower keeps blooming. Drop the next seed.
