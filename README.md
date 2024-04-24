# Reto_Fruitloops
# Flask API and Python Environment Setup

This repository contains a basic guide to set up a Flask API and Python environment. Follow these steps to get started with your project.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set Up a Virtual Environment](#2-set-up-a-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Configure Environment Variables](#4-configure-environment-variables)
- [Running the Flask App](#running-the-flask-app)
- [Project Configuration](#project-configuration)

## Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

- Python 3.x
- pip (Python package manager)

## Project Structure

```plaintext
FRUIT_LOOPS/
    env/
    src/
        routes/
        config.py
        extensions.py
        main.py
    .env
    .env.example
    requirements.txt
```

## Getting Started

# 1-clone-the-repository
  ```bash
  git clone -b python https://github.com/GabsCrisNav/Reto_Fruitloops.git

  cd Reto_Fruitloops
  ```

# 2-set-up-a-virtual-environment
  Create a virtual environment for your project to isolate dependencies:
  ```bash
  python -m venv venv
  ```

  Activate the virtual environment:

  On Windows:
  ```bash
  venv\Scripts\activate
  ```

  On macOS and Linux:
  ```bash
  source venv/bin/activate
  ```

# 3-install-dependencies

  Install the required packages from the requirements.txt file:
  ```bash
  pip install -r requirements.txt
  ```

# 4-configure-environment-variables

  Create a .env file in the project root and configure environment variables like the .env.example template

## Running the Flask App

  You can run the Flask app using the following command:
  ```bash
  python src/main.py
  ```

## Project Configuration
  You can configure various settings for your Flask app in the config.py file. Update this file with the object that suit your project's needs.