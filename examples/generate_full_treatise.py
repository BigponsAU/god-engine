"""Generate the full treatise in symbolic mode."""
from god_engine import GOD_Engine

if __name__ == "__main__":
    print("Flower-of-Life GOD Engine — full treatise (y′=0)")
    engine = GOD_Engine(y_prime=0.0)
    files = engine.generate_full_treatise(total_petals=100, output_dir="full_treatise_god_mode")
    print(f"Generated {len(files)} files in full_treatise_god_mode/")
    print("Compile any petal with: pdflatex petal_001.tex")
