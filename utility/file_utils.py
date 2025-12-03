import os
import subprocess

@staticmethod
def simulate_send_email(email_address, subject, message):
        """
        Sends a 'simulated' email in the form of adding an email message 
        to a text file.  The message will appear in the 'observer_emails.txt' 
        file within the 'output' directory of the current project directory.
        Args:
            email_address (str):  The email address to which the 'simulated' message is sent.
            subject (str):  The subject line for the 'simulated' message.
            message (str): The message body for the 'simulated' message.
        """
        directory = "output"
        filename = "observer_emails.txt"
        path = os.path.join(directory, filename)
        os.makedirs(directory, exist_ok=True)
        with open(path, "a") as file:
            file.write(f"---\nTo: {email_address}\nSubject: {subject}\nMessage: {message}\n---\n")

def run_system_command(user_input: str) -> str:
    command = f"echo {user_input}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def read_user_file(filename: str) -> str:
    base_path = "/tmp/uploads"
    file_path = os.path.join(base_path, filename)
    with open(file_path, 'r') as f:
        return f.read()