```python
import os
import subprocess

github_repository_link = "https://github.com/user/repo.git"  # replace with actual link
clone_command = f"git clone {github_repository_link}"
run_command = "python cleaned_code.py"
installation_requirements = "requirements.txt"

def run_existing_code():
    try:
        subprocess.check_call(["python", "existing_code.py"])
    except subprocess.CalledProcessError:
        return "Error in running existing_code.py"
    return "existing_code.py ran successfully"

def clean_code():
    try:
        subprocess.check_call(["python", "cleaned_code.py"])
    except subprocess.CalledProcessError:
        return "Error in running cleaned_code.py"
    return "cleaned_code.py ran successfully"

def check_missing_files():
    try:
        subprocess.check_call(["python", "missing_files.py"])
    except subprocess.CalledProcessError:
        return "Error in running missing_files.py"
    return "missing_files.py ran successfully"

def clone_repository():
    try:
        subprocess.check_call(clone_command.split())
    except subprocess.CalledProcessError:
        return "Error in cloning the repository"
    return "Repository cloned successfully"

def install_requirements():
    try:
        subprocess.check_call(["pip", "install", "-r", installation_requirements])
    except subprocess.CalledProcessError:
        return "Error in installing requirements"
    return "Requirements installed successfully"

def run_repository():
    try:
        subprocess.check_call(run_command.split())
    except subprocess.CalledProcessError:
        return "Error in running the repository"
    return "Repository ran successfully"

if __name__ == "__main__":
    print(run_existing_code())
    print(clean_code())
    print(check_missing_files())
    print(clone_repository())
    print(install_requirements())
    print(run_repository())
```