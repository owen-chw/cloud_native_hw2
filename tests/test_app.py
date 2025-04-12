import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import calculator

def test_add():
    calc = calculator()
    assert calc.addition(3,4) == 7