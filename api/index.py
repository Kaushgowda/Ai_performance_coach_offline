
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

# Import your backend handler
from backend import H


# Vercel Python entrypoint
class handler(H):
    pass