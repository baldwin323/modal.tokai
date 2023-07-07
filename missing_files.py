```python
import os

def check_missing_files():
    required_files = ["Prompt.md", "existing_code.py", "cleaned_code.py", "README.md", "run_instructions.py"]
    missing_files = []

    for file in required_files:
        if not os.path.isfile(file):
            missing_files.append(file)

    if missing_files:
        print("The following files are missing:")
        for file in missing_files:
            print(file)
    else:
        print("All required files are present.")

check_missing_files()
```