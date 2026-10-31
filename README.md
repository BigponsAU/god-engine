# Flower-of-Life √(3−4i) Cantor-Riemann GOD Engine

**A self-referential fractal framework for symbolic mathematical exploration.**

The engine generates inspectable, self-consistent LaTeX treatises (petals) using fractal sieving, golden-ratio algebra from the exact branches of √(3−4i), and an explicit **honesty dial** (`y′`).

## Honesty Dial (y′)

| Value | Mode | Behavior |
|-------|------|----------|
| `1.0` | Rigorous | Heuristic framing only. No classical-proof claims. |
| `0.0` | Symbolic / God | Every generated statement is declared true inside the petal. |
| (0,1) | Blended | Graded mixture (future extension). |

The dial is declared on every output so epistemic status is always transparent.

## Quick Start

```bash
git clone https://github.com/BigponsAU/god-engine.git
cd god-engine
pip install -e .

# Generate 5 petals in symbolic mode
python -m god_engine.core

# Or use the example
python examples/generate_full_treatise.py
```

## Core Algebraic Seed

The engine is grounded in the exact branches of √(3−4i):

\[
\sqrt{3-4i} = \pm \sqrt{-1+\sqrt{5}} \mp i \frac{2}{\sqrt{-1+\sqrt{5}}}
\]

These provide the golden-ratio pinning frequencies used for all Cantor-dust bridges inside the generated petals.

## What the Engine Is (and Is Not)

**It is:**
- A generative instrument that produces detailed, internally consistent symbolic narratives.
- A transparent dual-mode system (rigorous vs. symbolic).
- A living, self-referential framework that can expand its own treatise.

**It is not:**
- A classical theorem prover that delivers externally verifiable proofs of open Millennium Problems when `y′ = 1`.
- A replacement for traditional mathematical practice.

When `y′ = 1` the outputs are offered as powerful heuristics and visual models. When `y′ = 0` they are declared literal inside the closed petal.

## Repository Layout

```
god-engine/
├── src/god_engine/
│   ├── __init__.py
│   └── core.py          # Complete engine
├── examples/
│   └── generate_full_treatise.py
├── paper/
│   └── Flower_of_Life_Cantor_Riemann_Engine_Paper.tex
├── pyproject.toml
└── README.md
```

## License

MIT — use, modify, and extend freely.

---

> The flower keeps blooming. Drop the next seed.
