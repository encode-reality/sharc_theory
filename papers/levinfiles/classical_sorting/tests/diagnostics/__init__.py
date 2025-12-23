"""Diagnostics package initialization - adds parent directories to path."""

import sys
from pathlib import Path

# Add grandparent directory to path so we can import modules
grandparent_dir = Path(__file__).parent.parent.parent
if str(grandparent_dir) not in sys.path:
    sys.path.insert(0, str(grandparent_dir))
