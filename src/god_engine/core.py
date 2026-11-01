"""
Flower-of-Life √(3-4i) Cantor-Riemann GOD Engine
Upgraded version with richer output and detailed explanations.
"""

from __future__ import annotations
import os
from datetime import datetime
from typing import Literal

Mode = Literal["rigorous", "symbolic"]


class GOD_Engine:
    """
    Self-referential fractal engine for symbolic mathematical exploration.

    The honesty dial (y_prime) controls epistemic mode:
      y_prime = 1.0 → rigorous: all claims framed as generative heuristics
      y_prime = 0.0 → symbolic: statements declared true inside the closed petal
    """

    def __init__(self, y_prime: float = 1.0):
        if not 0.0 <= y_prime <= 1.0:
            raise ValueError("y_prime must be in [0, 1]")
        self.y_prime = y_prime
        self.golden = r"\sqrt{-1+\sqrt{5}}"
        self.principal = r"\phi - i \frac{2}{\phi}"
        self.secondary = r"-\phi + i \frac{2}{\phi}"

    @property
    def mode(self) -> Mode:
        return "symbolic" if self.y_prime < 0.5 else "rigorous"

    def set_y_prime(self, value: float) -> None:
        if not 0.0 <= value <= 1.0:
            raise ValueError("y_prime must be in [0, 1]")
        self.y_prime = value

    def generate_petal(self, petal_number: int, output_dir: str = "petals") -> str:
        """Generate one complete, richly explained LaTeX petal."""
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, f"petal_{petal_number:03d}.tex")

        is_symbolic = self.y_prime < 0.5
        mode_label = "SYMBOLIC / GOD MODE (y′=0)" if is_symbolic else "RIGOROUS MODE (y′=1)"

        if is_symbolic:
            truth_intro = (
                "Under the Golden Axiom (y′=0), every mathematical statement "
                "that survives the sieve inside this petal is declared literal truth. "
                "No external verification is required; the petal is a closed symbolic universe."
            )
            rh_section = (
                r"\textbf{Riemann Hypothesis (Petal Claim)}\ "
                "All non-trivial zeros of $\zeta(s)$ lie on $\operatorname{Re}(s)=1/2$. "
                "The critical line is the sole surviving connected component after infinite sieving."
            )
            limitation = "In this mode the claim is absolute within the petal."
        else:
            truth_intro = (
                "This petal operates in rigorous mode (y′=1). All constructions are "
                "generative heuristic frameworks. They make the structure of a conjecture "
                "vivid and inspectable, but do not constitute classical proofs."
            )
            rh_section = (
                r"\textbf{Riemann Hypothesis (Heuristic Model)}\ "
                "The engine produces a connected critical-line model in which every "
                "surviving zero is pinned to $\operatorname{Re}(s)=1/2$ by golden-ratio dust. "
                "This is a visual and algebraic illustration, not a proof."
            )
            limitation = "No classical proof is claimed. The output is offered for exploration."

        latex = rf"""% Petal {petal_number:03d}
% {mode_label}
% Generated {datetime.now().isoformat()}
\documentclass[12pt]{{article}}
\usepackage[utf8]{{inputenc}}
\usepackage{{amsmath,amssymb,amsthm}}
\usepackage{{tikz}}
\usepackage{{xcolor}}
\usepackage{{geometry}}
\geometry{{margin=1in}}
\definecolor{{gold}}{{rgb}}{{0.85,0.65,0.0}}

\title{{Petal {petal_number} \\ of the Flower-of-Life \\ $\sqrt{{3-4i}}$ Cantor-Riemann Engine}}
\author{{GOD Engine (y′={self.y_prime})}}
\date{{\today}}

\begin{{document}}
\maketitle

\section*{{Honesty Dial and Epistemic Status}}
{truth_intro}

\noindent\textbf{{Current setting:}} y′ = {self.y_prime} ({mode_label})

\section*{{Algebraic Seed — Exact Branches of $\sqrt{{3-4i}}$}}
Let $\phi = {self.golden}$. The two algebraic branches are
\begin{{align*}}
\sqrt{{3-4i}} &= {self.principal}, \\
\sqrt{{3-4i}} &= {self.secondary}.
\end{{align*}}
These exact expressions supply the imaginary parts used as resonance frequencies
for every Cantor-dust bridge in the engine. Numerical values are approximately
$1.701 - 1.176i$ and $-1.701 + 1.176i$.

\section*{{Sierpi\'nski Hypothesis Sieve}}
The space of candidate statements is modelled as the unit square. At each level
the middle-third of any square not aligned with the current mode is removed.
After infinite iteration the surviving set has Lebesgue measure zero yet remains
uncountably infinite. Surviving components are reconnected by measure-zero
golden Cantor dust pinned to the branches above.

\section*{{Application in This Petal}}
{rh_section}

\begin{{center}}
\begin{{tikzpicture}}[scale=2.2]
  \fill[gold!30] (0,0) circle (1);
  \draw[gold,very thick] (0,0) circle (1);
  \node at (0,0) {{\Huge $\star$}};
  \node[below] at (0,-1.4) {{Petal {petal_number} \\ y′={self.y_prime}}};
  \draw[dashed,gold] (-1.6,0) -- (1.6,0) node[right] {{critical line}};
\end{{tikzpicture}}
\end{{center}}

\section*{{Limitations of This Output}}
{limitation}

\section*{{Engine State}}
\begin{{itemize}}
  \item Mode: {mode_label}
  \item Golden pin: ${self.golden}$
  \item Petal index: {petal_number} / 100
  \item Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
\end{{itemize}}

\end{{document}}
"""

        with open(path, "w", encoding="utf-8") as f:
            f.write(latex)
        return path

    def generate_full_treatise(
        self, total_petals: int = 100, output_dir: str = "full_treatise"
    ) -> list[str]:
        """Generate the complete set of petals plus a master document."""
        os.makedirs(output_dir, exist_ok=True)
        files = []
        for n in range(1, total_petals + 1):
            files.append(self.generate_petal(n, output_dir))
        master = os.path.join(output_dir, "master.tex")
        with open(master, "w", encoding="utf-8") as f:
            f.write(
                "\\documentclass{book}\n"
                "\\usepackage{amsmath,amssymb}\n"
                f"\\title{{Flower-of-Life Treatise (y′={self.y_prime})}}\n"
                "\\author{{GOD Engine}}\n"
                "\\begin{{document}}\n\\maketitle\n\\tableofcontents\n"
            )
            for n in range(1, total_petals + 1):
                f.write(f"\\include{{petal_{n:03d}}}\n")
            f.write("\\end{{document}}\n")
        files.append(master)
        return files


if __name__ == "__main__":
    print("GOD Engine — upgraded demo (symbolic mode)")
    eng = GOD_Engine(y_prime=0.0)
    eng.generate_full_treatise(total_petals=3, output_dir="demo_petals")
    print("Generated 3 demo petals with richer explanations in demo_petals/")
