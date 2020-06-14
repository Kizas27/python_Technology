import os
import sys

print(f"PYTHONPATH value: {os.getenv('PYTHONPATH')}")
print("Trying to import examplepackage")
sys.path.append("../")

from veiksmai.veksmas import *
print(sudetis(2,1))
print(atimtis(2,1))
print("Success!")