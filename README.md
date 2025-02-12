# Password Strength Checker

This is a simple **Password Strength Checker** built using Python and Tkinter. It evaluates password security based on specific criteria such as length, uppercase/lowercase letters, numbers, and special characters. The application provides feedback on password strength through a graphical user interface (GUI).

## Project Overview

The Python Password Strength Checker GUI is an application designed to assess the strength of a given password. It provides visual feedback to users on whether their password is weak, moderate, or strong. The tool checks for factors such as length, character variety (uppercase, lowercase, numbers, and symbols), and the presence of common passwords or easily guessable patterns. Built with a graphical user interface (GUI), this project offers a simple, interactive way for users to verify the strength of their passwords.

Key features of the project include:

- A user-friendly interface where users can input their passwords.
- Real-time password strength assessment with feedback (weak, moderate, strong).
- Visual indicators like color changes to indicate password strength.
- Easy-to-use design with intuitive prompts for password criteria.

## Technologies Used

- **Python**: The core programming language used to build the application and implement the logic behind the password strength checker.
- **Tkinter**: A Python library for creating the graphical user interface (GUI), making the app user-friendly and interactive.
- **re (Regular Expressions)**: Used to check patterns within the password, such as the inclusion of uppercase letters, numbers, and special characters.
- **Tkinter's built-in widgets**: Buttons, labels, and entry fields to create the interactive GUI elements.

## Features
- **Graphical Interface**: Uses Tkinter for a simple UI.
- **Real-time Evaluation**: Checks password strength instantly.
- **Criteria-Based Strength Assessment**:
  - At least 8 characters
  - Includes uppercase and lowercase letters
  - Contains numbers
  - Has special characters
- **Alerts and Warnings**: Displays messages for feedback.

## Installation
Ensure you have Python installed. You can install Tkinter (if not pre-installed) using:
```sh
pip install tk
```

## Usage
1. Run the script:
```sh
python password_strength_checker.py
```
2. Enter a password in the input field.
3. Click "Check Strength" to evaluate.

## Images
![Demo 1](Demo/Demo1.PNG)
![Demo 2](Demo/Demo2.PNG)

## Contribution
Feel free to contribute by submitting issues or pull requests.
