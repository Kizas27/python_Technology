import os
import sys

print(f"PYTHONPATH value: {os.getenv('PYTHONPATH')}")
sys.path.append("../Data")
print(sys.path)
print(f"PYTHONPATH value: {os.getenv('PYTHONPATH')}")

from Data.veiksmai import *
print(sudetis(2,1))
print(atimtis(2,1))
print(daugyba(2,2))
print(dalyba(10,2))

print("Success!")

"""kai palediziu exe failiuka
Error loading Python DLL 'C:\Users\Vaidas\Desktop\python_Technology\Project\build\main\python38.dll'.
LoadLibrary: The specified module could not be found.
"""