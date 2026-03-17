"""Root conftest for quantum-foundations-demo: adds src/ to the import path."""

import sys
from pathlib import Path

# Add src/ directory so `quantum_demo` package is importable
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
