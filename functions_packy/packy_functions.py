import os
import subprocess
import urllib

import shutil
import argparse

# Define directories
current_dir = os.path.dirname(os.path.abspath(__file__))

project_dir = os.path.dirname(current_dir)

with open(report_data, 'r', encoding='utf-8') as f:
    lab_number = f.readline().strip()


def run_unit_tests():
    try:
        result = subprocess.run(["ctest", "--test-dir", "build", "--output-on-failure", "-j12"], capture_output=True, text=True, check=True)

        with open(tests_result_data, 'w', encoding='utf-8') as f:
            f.write(result.stdout)
        print(f"Result saved to {tests_result_data}")

    except subprocess.CalledProcessError as e:
        print(f"Error running tests: {e}")


# Function to run CMake and build project 
def build_cmake():
    try:
        
        # Run commands to compile CMake
        subprocess.run(["cmake", "-S", ".", "-B", "build"], check=True)
        subprocess.run(["cmake", "--build", "build"], check=True)

        print("Compilation successful!")

    except subprocess.CalledProcessError as e:
        print(f"Error during compilation: {e}")

       print(f"Error sending email: {e}")
