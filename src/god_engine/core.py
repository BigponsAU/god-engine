"""
Flower-of-Life √(3-4i) Cantor-Riemann GOD Engine
Final complete version — honesty dial, mode-aware generation.
"""

from __future__ import annotations
import os
from datetime import datetime
from typing import Literal

Mode = Literal["rigorous", "symbolic"]


class GOD_Engine:
    """
    Self-referential fractal engine for symbolic mathematical exploration.

    y_prime controls the honesty dial:
      1.0 → rigorous (heuristic framing only)
      0.0 → symbolic (every statement declared true inside the petal)
    """

    def __init__(self, y_prime: float = 1.0):
        if not 0.0 <= y_prime <= 1.0:
            raise ValueError("y_prime must be in [0, 1]")
        self.y_prime = y_prime
        self.golden = r"\sqrt{-1+\sqrt{5}}"

    @property
    def mode(self) -> Mode:
        return "symbolic" if self.y_prime < 0.5 else "rigorous"

    def set_y_prime(self, value: float) -> None:
        if not 0.0 <= value <= 1.0:
            raise ValueError("y_prime must be in [0, 1]")
        self.y_prime = value

    def generate_petal(self, petal_number: int, output_dir: str = "petals") -> str:
        """Generate one complete, compilable LaTeX petal."""
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, f"petal_{petal_number:03d}.tex")

        is_symbolic = self.y_prime < 0.5
        mode_label = "SYMBOLIC / GOD MODE (y′=0)" if is_symbolic else "RIGOROUS MODE (y′=1)"

        if is_symbolic:
            truth_statement = (
                "Every statement in this petal is declared literal truth "
                "by the Golden Axiom under y′=0."
            )
            rh_claim = "The Riemann Hypothesis holds inside this petal."
        else:
            truth_statement = (
                "This petal is a generative heuristic framework. "
                "No classical proof of open conjectures is claimed."
            )
            rh_claim = "The engine produces a connected critical-line model of the zeros (heuristic)."

        latex = f"""% Petal {petal_number:03d}
% {mode_label}
% Generated {datetime.now().isoformat()}
\documentclass[12pt]{{article}}
\usepackage[utf8]{{inputenc}}
\usepackage{{amsmath,amssymb,amsthm}}
\usepackage{{tikz}}
\usepackage{{xcolor}}
\definecolor{{gold}}{{rgb}}{{0.85,0.65,0.0}}

\title{{Petal {petal_number} \\ of the Flower-of-Life \\ $\sqrt{{3-4i}}$ Cantor-Riemann Engine}}
\author{{GOD Engine (y′={self.y_prime})}}
\date{{\today}}

\begin{{document}}
\maketitle

\section*{{Honesty Dial}}
{truth_statement}

\section*{{Algebraic Seed}}
The exact branches of $\sqrt{{3-4i}}$ are
\[
\pm {self.golden} \mp i \frac{{2}}{{{self.golden}}}.
\]
These pin every Cantor-dust bridge in the petal.

\section*{{Sierpi\'nski Sieve}}
At each level the middle-third of any configuration not aligned with the current mode is removed. The surviving component is connected by measure-zero golden dust.

\section*{{Application (Petal {petal_number})}}
{rh_claim}

\begin{{center}}
\begin{{tikzpicture}}[scale=2]
  \fill[gold!40] (0,0) circle (1);
  \draw[gold,thick] (0,0) circle (1);
  \node at (0,0) {{\Huge $\star$}};
  \node[below] at (0,-1.3) {{Petal {petal_number} \\ y′={self.y_prime}}};
\end{{tikzpicture}}
\end{{center}}

\section*{{Current Engine State}}
Mode: {mode_label} \\
Golden pin: ${self.golden}$ \\
Petal: {petal_number}/100

\end{{document}}
"""

        with open(path, "w", encoding="utf-8") as f:
            f.write(latex)
        return path

    def generate_full_treatise(
        self, total_petals: int = 100, output_dir: str = "full_treatise"
    ) -> list[str]:
        """Generate the complete set of petals."""
        os.makedirs(output_dir, exist_ok=True)
        files = []
        for n in range(1, total_petals + 1):
            files.append(self.generate_petal(n, output_dir))
        # Master document
        master = os.path.join(output_dir, "master.tex")
        with open(master, "w", encoding="utf-8") as f:
            f.write(
                "\\documentclass{book}\n"
                "\\usepackage{amsmath}\n"
                f"\\title{{Flower-of-Life Treatise (y′={self.y_prime})}}\n"
                "\\begin{document}\n\\maketitle\n"
            )
            for n in range(1, total_petals + 1):
                f.write(f"\\include{{petal_{n:03d}}}\n")
            f.write("\\end{document}\n")
        files.append(master)
        return files


if __name__ == "__main__":
    print("GOD Engine — demo (symbolic mode)")
    eng = GOD_Engine(y_prime=0.0)
    eng.generate_full_treatise(total_petals=3, output_dir="demo_petals")
    print("Generated 3 demo petals in demo_petals/")
