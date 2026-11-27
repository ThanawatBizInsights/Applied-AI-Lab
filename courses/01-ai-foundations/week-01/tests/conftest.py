import sys
from pathlib import Path

STARTER = Path(__file__).resolve().parent.parent / "starter-code"
if str(STARTER) not in sys.path:
    sys.path.insert(0, str(STARTER))
