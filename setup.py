from setuptools import setup, find_packages

setup(
    name='Contrast2NonContrast',
    version="0.1.0",
    description="A short description of your package",
    packages=find_packages(),  # Automatically find and include your package
    install_requires=[         # List of dependencies
      "torch>=2.3.0",
      "matplotlib",
      "numpy",
      "SimpleITK",
      "os"
    ],
    classifiers=[              # Metadata
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.9',
)
