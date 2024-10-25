import os
import subprocess
import urllib

# import library for email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import shutil
import argparse

# Define directories
current_dir = os.path.dirname(os.path.abspath(__file__))

project_dir = os.path.dirname(current_dir)
report_dir = os.path.join(project_dir, "report")
task_condition_dir = os.path.join(report_dir, "task_condition")
tests_result_dir = os.path.join(report_dir, "tests_result")

# Define files path
data_packy_file = os.path.join(project_dir, "data_packy.txt")
report_data = os.path.join(report_dir, "data.txt")
task_condition_data = os.path.join(task_condition_dir, "data.txt")
tests_result_data = os.path.join(tests_result_dir, "unit_result.txt")
auto_report_file = os.path.join(report_dir, "auto_report.py")

# main_cpp_file = os.path.join(project_dir, "build/src/main") 

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

# Function to create report docx file
def create_report():
   
    # Enter lab info
    subprocess.run(['nvim', f'{report_data}'])
    
    # Enter lab task condition
    subprocess.run(['nvim', f'{task_condition_data}'])

    # Save results of unit tests
    run_unit_tests()

    # Creating report docx file
    subprocess.run(['python3', f'{auto_report_file}'])

# Open created report in LibreOffice
def run_verify():
    try:
        subprocess.run(['libreoffice', '--writer', f'{report_dir}/АП_РІ-12_Грушевський_ЛР-{lab_number}.docx'])

    except subprocess.CalledProcessError as e:
        print(f"Error opening: {e}")



def send_email():
    # Get user's info
    with open(data_packy_file, 'r', encoding='utf-8') as f:
        sender_email = f.readline().strip()
        sender_password = f.readline().strip()
        receiver_email = f.readline().strip()

    # Info for email
    subject = f"АП РІ-12 Грушевський ЛР-{lab_number}"
    attachment_path = os.path.join(report_dir, f"АП_РІ-12_Грушевський_ЛР-{lab_number}.docx")
    body = "Грушевський Іван РІ-12"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if os.path.isfile(attachment_path):  # Check if the file exists
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "vnd.openxmlformats-officedocument.wordprocessingml.document")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)

            # Get the filename
            filename = os.path.basename(attachment_path)
            print(f"Attachment Filename: {filename}")  # Debugging line

            # Use filename directly for the header
            part.add_header(
                "Content-Disposition",
                'attachment; filename="%s"' % os.path.basename(attachment_path))
            msg.attach(part)
    else:
        print(f"Error: File does not exist: {attachment_path}")
        return

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
