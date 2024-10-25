import argparse
from functions_packy.packy_functions import build_cmake, create_report, run_verify, send_email

def main():

    parser = argparse.ArgumentParser(description="Packy - your friendly helper in automated developing")

    # Adding command-line arguments
    # parser.add_argument('-h', '--help', action='store_true', help='Packy help info')
    parser.add_argument('-c', '--cmake', action='store_true', help='Build project with CMake')

    args = parser.parse_args()

    if args.cmake:
        print("Building project with CMake...")
        build_cmake()
        
if __name__ == "__main__":
    main()
