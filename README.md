# Multi-Unit Converter

A simple command-line tool for converting various units such as temperature, distance, currency, and data sizes. This project demonstrates agile methodologies, Git workflows, and CI/CD integration using GitHub Actions.

## Overview

The Multi-Unit Converter is a Python-based CLI application that allows users to easily convert between different units. It includes conversions for:
- **Temperature**: Celsius ↔ Fahrenheit
- **Distance**: Kilometers ↔ Miles
- **Currency**: EUR ↔ USD (with a fixed exchange rate)
- **Data Size**: MB ↔ GB (optional)

This project also serves as a learning platform for implementing best practices in software development, including unit testing, version control with Git, and continuous integration.

## Features

- **User-Friendly CLI**: Provides clear instructions and help options for users.
- **Input Validation**: Ensures that user inputs are valid and provides helpful error messages.
- **Modular Design**: Conversion logic is separated into distinct modules.
- **CI/CD Pipeline**: Automatically runs tests via GitHub Actions on each push or pull request.

## Getting Started

### Installation

1. **Clone the repository:**

   git clone https://github.com/yourusername/multi-unit-converter.git

2. **Navigate to the folder:**

   cd multi-unit-converter

3. **Test the some features:**

   *** Celsius to Fahrenheit:*** 
   python3 converter.py temp --mode c2f 20.0

   *** Fahrenheit to Celsius ***
   python3 converter.py temp --mode f2c 68.0



