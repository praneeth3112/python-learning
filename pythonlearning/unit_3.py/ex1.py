# Experiment 8
# File System Simulator
import os

print("=========================================")
print(" File System Simulator")
print("=========================================\n")

filename = "student.txt"
new_filename = "student_record.txt"

# Create and Write
with open(filename, "w") as file:
    file.write("Operating Systems Lab\n")
    file.write("Experiment 8\n")
    file.write("File System Simulator\n")
print("File Created Successfully.")

# Append Data
with open(filename, "a") as file:
    file.write("Python File Handling Example\n")
print("Data Appended Successfully.")

# Read File
print("\nReading File Contents:\n")
with open(filename, "r") as file:
    print(file.read())

# Rename File
os.rename(filename, new_filename)
print("File Renamed Successfully.")

# Delete File
os.remove(new_filename)
print("File Deleted Successfully.")

print("\nExperiment Completed Successfully.")