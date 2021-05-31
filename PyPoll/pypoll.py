import csv
from genericpath import exists
import os

election_data_csv = os.path.join("Resources","election_data.csv")

if (not os.path.exists(election_data_csv)):
    print("\nFile not found")
    print(f"Expected to find /Resources/election_data.csv \nin current working directory ({os.getcwd()})")
else:
    pass

