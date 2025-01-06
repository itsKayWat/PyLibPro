#!/usr/bin/env python3

import subprocess
import sys
import os

def install_requirements():
    """Install required packages for PyLibPro"""
    print("Setting up PyLibPro...")
    
    requirements = [
        'colorama',    # Terminal colors
        'logging',     # Logging functionality
    ]
    
    for package in requirements:
        try:
            print(f"\nInstalling {package}...")
            subprocess.check_call([
                sys.executable, 
                "-m", 
                "pip", 
                "install", 
                package
            ])
        except Exception as e:
            print(f"Error installing {package}: {e}")
            
    print("\nSetup complete! Run 'python lib-collect.py' to start")

if __name__ == "__main__":
    install_requirements()