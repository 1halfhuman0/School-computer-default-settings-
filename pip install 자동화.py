import subprocess
import sys

def install_requirements(file_path):
    try:
        with open(file_path, 'r') as file:
            packages = [line.strip() for line in file if line.strip() and not line.startswith('#')]
            for package in packages:
                print(f"Installing package: {package}")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print("All packages installed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    requirements_file = '기본세팅 설정/requirements.txt'
    install_requirements(requirements_file)
