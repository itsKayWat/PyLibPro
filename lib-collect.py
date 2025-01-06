#!/usr/bin/env python3

"""
🌈 ML Library Collection Manager

🔵 Purpose:
- Flexible installer for machine learning libraries
- Manages different categories of ML tools
- Provides size estimates and organized installation

🟡 Use Cases:
1. Data Science Setup:
   - Install core frameworks for new project
   - Set up visualization tools for data analysis
   - Configure NLP libraries for text processing

2. Teaching Environment:
   - Batch install libraries for classroom
   - Set up consistent environments for students
   - Manage library versions for coursework

3. Production Deployment:
   - Select specific libraries for deployment
   - Manage dependencies systematically
   - Track installations with logging
"""

import subprocess
import os
import sys
import logging
from typing import Dict, List, Set
from datetime import datetime

class MLLibraryManager:
    def __init__(self):
        """
        🔵 Initialize Manager:
        - Creates directory structure
        - Defines library categories and sizes
        - Sets up logging system
        
        🟡 Example Structure:
        ml_libraries/
        ├── logs/
        │   └── installation_20240105.log
        └── requirements/
            └── installed_packages.txt
        """
        self.base_dir = "ml_libraries"
        self.libraries = {
            "1_core_frameworks": {
                "tensorflow": "~2GB",    # 🟢 Deep Learning & ML
                "torch": "~4GB",         # 🟢 PyTorch for Deep Learning
                "scikit-learn": "~300MB",# 🟢 Traditional ML
                "keras": "~100MB",       # 🟢 High-level Neural Networks
                "jax": "~600MB",         # 🟢 Numerical Computing
                "xgboost": "~200MB",     # 🟢 Gradient Boosting
            },
            "2_visualization": {
                "matplotlib": "~50MB",    # 🟣 Basic Plotting
                "plotly": "~100MB",       # 🟣 Interactive Viz
                "seaborn": "~20MB",       # 🟣 Statistical Viz
                "bokeh": "~80MB",         # 🟣 Web-based Viz
                "altair": "~30MB",        # 🟣 Declarative Viz
            },
            "3_nlp": {
                "transformers": "~5GB",    # 🟡 Hugging Face Models
                "spacy": "~1GB",           # 🟡 NLP Processing
                "nltk": "~500MB",          # 🟡 Text Processing
                "gensim": "~200MB",        # 🟡 Topic Modeling
                "sentence-transformers": "~1GB", # 🟡 Text Embeddings
            }
        }
        self.setup_logging()

    def setup_logging(self):
        """
        🔵 Logging Configuration:
        - Creates timestamped log files
        - Records all installations
        - Tracks errors and successes
        
        🟡 Log Example:
        2024-01-05 14:30:22 - INFO - Installing tensorflow...
        2024-01-05 14:35:45 - SUCCESS - tensorflow installed
        """
        log_dir = os.path.join(self.base_dir, "logs")
        os.makedirs(log_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(log_dir, f"installation_{timestamp}.log")
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )

    def display_menu(self):
        """Main menu display with descriptions"""
        print("\n" + "="*50)
        print("ML Library Installation Manager")
        print("="*50)
        print("Available Options:")
        print("\n1. Install All Libraries (~15GB total)")
        print("   → Complete setup for ML development")
        print("   → Includes all frameworks, visualization, and NLP tools")
        print("   → Best for full development environments")
        print("\n2. Install by Category")
        print("   → Choose specific domains (ML, Visualization, NLP)")
        print("   → Optimized for different use cases:")
        print("     • ML/AI Development: Core Frameworks")
        print("     • Data Analysis: Visualization")
        print("     • Text Processing: NLP")
        print("\n3. Install Individual Libraries")
        print("   → Pick specific libraries you need")
        print("   → Save space by selecting only required tools")
        print("   → Custom installation for specific projects")
        print("\n0. Exit")
        print("="*50)

    def display_categories(self):
        """Category display with use cases"""
        print("\nAvailable Categories:")
        print("\n1. Core Frameworks (~7.2GB)")
        print("   → Machine Learning & Deep Learning")
        print("   • TensorFlow: Neural Networks, Deep Learning")
        print("   • PyTorch: Research, Deep Learning")
        print("   • Scikit-learn: Traditional ML, Data Mining")
        print("   Best for: AI Development, Model Training")
        
        print("\n2. Visualization (~280MB)")
        print("   → Data Visualization & Analysis")
        print("   • Matplotlib: Static Plots")
        print("   • Plotly: Interactive Dashboards")
        print("   • Seaborn: Statistical Visualization")
        print("   Best for: Data Analysis, Reporting")
        
        print("\n3. NLP (~7.7GB)")
        print("   → Natural Language Processing")
        print("   • Transformers: Language Models, BERT")
        print("   • SpaCy: Text Processing, Named Entities")
        print("   • NLTK: Text Analysis, Linguistics")
        print("   Best for: Text Analysis, Language Processing")
        
        print("\n0. Back to main menu")

    def display_libraries(self, category):
        """Library display with descriptions"""
        libs = list(self.libraries[category].items())
        category_name = category[2:].replace('_', ' ').title()
        
        print(f"\nLibraries in {category_name}:")
        if category.startswith("1_"):  # Core Frameworks
            print("\nMachine Learning & Deep Learning Libraries:")
            for i, (lib, size) in enumerate(libs, 1):
                desc = {
                    "tensorflow": "→ Google's deep learning framework",
                    "torch": "→ Facebook's PyTorch for research & production",
                    "scikit-learn": "→ Traditional ML algorithms & tools",
                    "keras": "→ High-level neural network API",
                    "jax": "→ Automatic differentiation & XLA",
                    "xgboost": "→ Gradient boosting framework"
                }.get(lib, "")
                print(f"{i}. {lib} ({size})\n   {desc}")
                
        elif category.startswith("2_"):  # Visualization
            print("\nData Visualization Tools:")
            for i, (lib, size) in enumerate(libs, 1):
                desc = {
                    "matplotlib": "→ Basic plotting library",
                    "plotly": "→ Interactive visualization",
                    "seaborn": "→ Statistical data visualization",
                    "bokeh": "→ Web-based visualization",
                    "altair": "→ Declarative visualization"
                }.get(lib, "")
                print(f"{i}. {lib} ({size})\n   {desc}")
                
        elif category.startswith("3_"):  # NLP
            print("\nNatural Language Processing Tools:")
            for i, (lib, size) in enumerate(libs, 1):
                desc = {
                    "transformers": "→ State-of-the-art NLP models",
                    "spacy": "→ Industrial-strength NLP",
                    "nltk": "→ Natural Language Toolkit",
                    "gensim": "→ Topic modeling & document similarity",
                    "sentence-transformers": "→ Text embeddings & similarity"
                }.get(lib, "")
                print(f"{i}. {lib} ({size})\n   {desc}")
        
        print("\n0. Back to categories")
        return libs

    def calculate_category_size(self, category: str) -> str:
        """Calculate total size for a category."""
        return self.calculate_size(set(self.libraries[category].keys()))

    def calculate_size(self, libraries: Set[str]) -> str:
        """Calculate total size for selected libraries."""
        total_mb = 0
        for category in self.libraries.values():
            for lib, size in category.items():
                if lib in libraries:
                    size_str = size.lower()
                    if 'gb' in size_str:
                        mb = float(size_str.replace('~', '').replace('gb', '')) * 1024
                    else:
                        mb = float(size_str.replace('~', '').replace('mb', ''))
                    total_mb += mb
        
        if total_mb > 1024:
            return f"~{total_mb/1024:.1f}GB"
        return f"~{total_mb:.0f}MB"

    def install_libraries(self, selected: Set[str]):
        """Install selected libraries using pip."""
        for lib in selected:
            try:
                print(f"\nInstalling {lib}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
                print(f"Successfully installed {lib}")
            except subprocess.CalledProcessError as e:
                print(f"Error installing {lib}: {str(e)}")
            except Exception as e:
                print(f"Unexpected error installing {lib}: {str(e)}")

    def run(self):
        """
        Main run loop for the library manager.
        
        🟥 Process Flow:
        1. Display main menu
        2. Handle user selection
        3. Install selected libraries
        4. Repeat until exit
        """
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (0-3): ")

            if choice == "0":
                print("Exiting...")
                break

            elif choice == "1":
                # Install all libraries
                all_libs = set()
                for category in self.libraries.values():
                    all_libs.update(category.keys())
                total_size = self.calculate_size(all_libs)
                if input(f"\nInstall all libraries? Total size: {total_size} (y/n): ").lower() == 'y':
                    self.install_libraries(all_libs)

            elif choice == "2":
                # Install by category
                while True:
                    self.display_categories()
                    cat_choice = input("\nSelect category (0-3): ")
                    if cat_choice == "0":
                        break
                    category = f"{cat_choice}_" + list(self.libraries.keys())[int(cat_choice)-1][2:]
                    if category in self.libraries:
                        size = self.calculate_category_size(category)
                        if input(f"\nInstall {category[2:]}? Size: {size} (y/n): ").lower() == 'y':
                            self.install_libraries(set(self.libraries[category].keys()))

            elif choice == "3":
                # Install individual libraries
                while True:
                    self.display_categories()
                    cat_choice = input("\nSelect category (0-3): ")
                    if cat_choice == "0":
                        break
                    category = f"{cat_choice}_" + list(self.libraries.keys())[int(cat_choice)-1][2:]
                    if category in self.libraries:
                        while True:
                            libs = self.display_libraries(category)
                            lib_choice = input("\nSelect library (0 to go back): ")
                            if lib_choice == "0":
                                break
                            try:
                                idx = int(lib_choice) - 1
                                if 0 <= idx < len(libs):
                                    lib_name = libs[idx][0]
                                    if input(f"\nInstall {lib_name}? Size: {libs[idx][1]} (y/n): ").lower() == 'y':
                                        self.install_libraries({lib_name})
                            except ValueError:
                                print("Invalid input")

def main():
    """
    🔵 Main Application Entry:
    
    🟡 Usage Scenarios:
    1. New Project Setup:
       python lib-collect.py
       > Choose option 2
       > Select Core Frameworks
       
    2. Visualization Tools:
       python lib-collect.py
       > Choose option 2
       > Select Visualization
       
    3. NLP Workspace:
       python lib-collect.py
       > Choose option 2
       > Select NLP
       
    4. Custom Environment:
       python lib-collect.py
       > Choose option 3
       > Select specific libraries
    """
    try:
        manager = MLLibraryManager()
        manager.run()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
