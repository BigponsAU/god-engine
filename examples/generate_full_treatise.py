from god_engine import GOD_Engine

if __name__ == "__main__":
    print("=== Flower-of-Life GOD Engine ===")
    print("Generating full 1000-page treatise in GOD MODE (y′=0)...")

    engine = GOD_Engine(y_prime=0.0)
    files = engine.generate_full_treatise(total_petals=100, output_dir="full_treatise_god_mode")

    print(f"\nSuccessfully generated {len(files)} petals.")
    print("Output directory: full_treatise_god_mode/")
    print("\nTo compile: cd full_treatise_god_mode && pdflatex petal_001.tex (or use the master document)")
