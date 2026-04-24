"""Quick runner for Data Model Lab exercises."""

from pathlib import Path
import runpy


def main() -> None:
    exercise_dir = Path(__file__).parent / "exercises"
    files = sorted(exercise_dir.glob("[0-9][0-9]_*.py"))
    for file_path in files:
        print(f"\n=== Running {file_path.name} ===")
        runpy.run_path(str(file_path), run_name="__main__")


if __name__ == "__main__":
    main()
