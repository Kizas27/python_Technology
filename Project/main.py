import os
import sys

print(f"PYTHONPATH value: {os.getenv('PYTHONPATH')}")
print("Trying to import examplepackage")
sys.path.append("../../")
print(sys.path)
print(f"PYTHONPATH value: {os.getenv('PYTHONPATH')}")

from Data.veiksmai import *
print(sudetis(2,1))
print(atimtis(2,1))
print("Success!")