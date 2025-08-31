# Project Setup Guide

This guide will help you set up a Python virtual environment, activate it, and install the required dependencies using `requirements.txt`.

## 1. Create a Virtual Environment

Open your terminal and navigate to the project directory. Then, run the following command to create a new virtual environment named `venv`:

```bash
python3 -m venv venv
```

## 2. Activate the Virtual Environment

- **On Linux or macOS:**

    ```bash
    source venv/bin/activate
    ```

- **On Windows:**

    ```cmd
    venv\Scripts\activate
    ```

## 3. Install the Requirements

After activating the virtual environment, install the required dependencies:

```bash
pip install -r requirements.txt
```

## 4. You're All Set!

Now you can run or develop your project in your isolated environment.

---

**Note:**  
If you ever want to deactivate the virtual environment, simply run:

```bash
deactivate
```
