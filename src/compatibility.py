```python
import platform

def check_compatibility():
    """
    Function to check platform compatibility.
    """
    os_info = platform.uname()
    os_name = os_info.system
    os_version = os_info.version

    compatible_os = ['Windows', 'Darwin', 'Linux']
    if os_name not in compatible_os:
        raise Exception(f'Unsupported operating system: {os_name}. The app supports only Windows, macOS, and Linux.')

    print(f'Running on {os_name} version {os_version}. Compatibility check passed.')

if __name__ == "__main__":
    check_compatibility()
```