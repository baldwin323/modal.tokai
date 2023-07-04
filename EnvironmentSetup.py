```python
import os
import subprocess

def setup_environment():
    # Check if Conda is installed
    try:
        subprocess.check_output("conda --version", shell=True)
    except subprocess.CalledProcessError:
        print("Conda is not installed. Please install Conda.")
        return

    # Create a new Conda environment for the app
    env_name = "app_env"
    try:
        subprocess.check_output(f"conda create --name {env_name}", shell=True)
    except subprocess.CalledProcessError:
        print("Failed to create a new Conda environment.")
        return

    # Activate the new Conda environment
    try:
        subprocess.check_output(f"conda activate {env_name}", shell=True)
    except subprocess.CalledProcessError:
        print("Failed to activate the new Conda environment.")
        return

    print("Environment setup completed successfully.")

if __name__ == "__main__":
    setup_environment()
```