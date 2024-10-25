import argparse
from functions_packy.packy_functions import build_cmake, create_report, run_verify, send_email

def main():

    parser = argparse.ArgumentParser(description="Packy - your friendly helper in passing labs")

    # Adding command-line arguments
    # parser.add_argument('-h', '--help', action='store_true', help='Packy help info')
    parser.add_argument('-c', '--cmake', action='store_true', help='Build project with CMake')
    parser.add_argument('-r', '--report', action='store_true', help='Creating report docx file')
    parser.add_argument('-v', '--verify', action='store_true', help='Verify report data')
    parser.add_argument('-e', '--email', action='store_true', help='Send email with the report')

    args = parser.parse_args()

    if args.cmake:
        print("Building project with CMake...")
        build_cmake()

    if args.report:
        print("Start creating report...\n")
        create_report()

    if args.verify:
        run_verify()

    if args.email:
        print("Sending report...")
        send_email()
        
if __name__ == "__main__":
    main()
