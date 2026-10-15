from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "provided"
    / "DS1_material_properties_5500.csv"
)

OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def validate_material_data():
    df = pd.read_csv(DATA_FILE)

    checks = {
        "Missing formation energy":
            df["formation_energy_per_atom_eV"].isna(),

        "Missing bulk modulus":
            df["bulk_modulus_GPa"].isna(),

        "Missing shear modulus":
            df["shear_modulus_GPa"].isna(),

        "Missing Poisson ratio":
            df["poisson_ratio"].isna(),

        "Missing density":
            df["density_g_cm3"].isna(),

        "Invalid Poisson ratio":
            (df["poisson_ratio"] <= -1)
            | (df["poisson_ratio"] >= 0.5),

        "Non-positive bulk modulus":
            df["bulk_modulus_GPa"] <= 0,

        "Non-positive shear modulus":
            df["shear_modulus_GPa"] <= 0,

        "Non-positive density":
            df["density_g_cm3"] <= 0,

        "Negative band gap":
            df["band_gap_eV"] < 0,

        "Negative energy above hull":
            df["energy_above_hull_eV"] < 0,
    }

    results = []

    print("Total material records:", len(df))
    print("\n--- Material Physics Validation ---")

    for name, condition in checks.items():
        count = int(condition.sum())
        print(f"{name}: {count}")

        results.append({
            "check": name,
            "records_flagged": count
        })

    report = pd.DataFrame(results)

    output_file = OUTPUT_DIR / "material_validation_report.csv"
    report.to_csv(output_file, index=False)

    print("\nValidation completed.")
    print("Report saved to:", output_file)


if __name__ == "__main__":
    validate_material_data()