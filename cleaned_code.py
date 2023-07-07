```python
import os
import autopep8

# Load the existing code
with open('existing_code.py', 'r') as file:
    existing_code = file.read()

# Clean up the code using autopep8
cleaned_code = autopep8.fix_code(existing_code)

# Write the cleaned code to cleaned_code.py
with open('cleaned_code.py', 'w') as file:
    file.write(cleaned_code)

# Check for missing files
required_files = ['existing_code.py', 'cleaned_code.py', 'missing_files.py', 'README.md', 'run_instructions.py']
for file in required_files:
    if not os.path.isfile(file):
        open(file, 'w').close()

print("Code cleanup completed and missing files added.")
```