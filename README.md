
## 🏠🤖Intelligent Hostel Management System (IHMS)

## Overview

The Intelligent Hostel Management System (IHMS) is a Python-based command-line application designed to simplify hostel administration and student management. The system allows wardens to manage hostel operations such as student registration, room allocation, and record viewing while maintaining secure login authentication.

IHMS integrates security features, voice feedback, and terminal-style interface animations to create an interactive hostel management environment.

## Features

### 🔐 Secure Login System
- Passwords stored using SHA-256 hashing
- Limited login attempts for security

### 👨‍💼 Warden Management

- Warden registration
- View warden details

### 👨‍🎓 Student Management

- Register male and female students
- Assign block and room numbers
- Search student records
- View registered student details

### 🏠 Room Allocation System

- Detects if a room is full
- Suggests available rooms

### 🔎 Student Search

- Search student by name

### 📊 Statistics

- Total registered boys
- Total registered girls

### 🔊 Voice Assistance

- System welcome voice using Text-to-Speech

### 🎨 Terminal Interface

- Colored terminal output
- Animated system initialization

## Technologies Used

- Python
- hashlib – Password encryption
- getpass – Secure password input
- time – System loading animation
- colorama – Colored terminal interface
- pyttsx3 – Text-to-speech voice feedback
## Project Structure
```bash 
IHMS/
│
├── ihms.py        # Main Python program
├── README.md      # Project documentation
```
## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/IHMS.git
cd IHMS
```
### 2. Install Required Libraries
```bash
pip install colorama
pip install pyttsx3
pip install hashlib
pip install getpass
pip install os 
pip install time
```
### 3.Run the Program
```bash
python ihms.py
```

## System Workflow

- User registers with username and password.
- Password is securely stored using SHA-256 hashing.
- User logs into the system.
- System initializes and displays the IHMS dashboard.
- User selects between:
- Warden Management
- Student Management
- Students can be registered, viewed, searched, and counted.
## Example Menu
#### INTELLIGENT HOSTEL MANAGEMENT SYSTEM

##### 1. Warden
##### 2. Student
##### 3. Exit


