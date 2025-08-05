#!/usr/bin/env python3
"""
Setup script for Jupyter notebook environment
"""
import subprocess
import sys
import os

def run_command(command):
    """Run a command and return the result"""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error: {e.stderr}")
        return None

def main():
    print("Setting up Jupyter notebook environment...")
    
    # Check if Python is installed
    python_version = run_command("python --version")
    if python_version:
        print(f"Python version: {python_version.strip()}")
    else:
        print("Python not found. Please install Python 3.8+ first.")
        return
    
    # Create virtual environment
    print("Creating virtual environment...")
    if not os.path.exists("venv"):
        venv_result = run_command("python -m venv venv")
        if venv_result is None:
            print("Failed to create virtual environment")
            return
        print("Virtual environment created successfully")
    else:
        print("Virtual environment already exists")
    
    # Activate virtual environment and install packages
    print("Installing required packages...")
    
    # For Windows
    if os.name == 'nt':
        pip_install = "venv\\Scripts\\pip install -r requirements.txt"
        python_path = "venv\\Scripts\\python.exe"
    else:
        pip_install = "venv/bin/pip install -r requirements.txt"
        python_path = "venv/bin/python"
    
    install_result = run_command(pip_install)
    if install_result:
        print("Packages installed successfully")
    else:
        print("Failed to install packages")
        return
    
    # Install Jupyter kernel
    print("Installing Jupyter kernel...")
    kernel_install = f"{python_path} -m ipykernel install --user --name=venv --display-name='Python (venv)'"
    kernel_result = run_command(kernel_install)
    if kernel_result:
        print("Jupyter kernel installed successfully")
    else:
        print("Failed to install Jupyter kernel")
    
    print("\nSetup complete! You can now:")
    print("1. Open any .ipynb file in Cursor")
    print("2. Select the 'Python (venv)' kernel when prompted")
    print("3. Run cells using Shift+Enter or the Run button")
    print("4. Use Ctrl+Shift+P and type 'Jupyter: Create Interactive Window' for interactive Python")

if __name__ == "__main__":
    main() 