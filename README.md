# Student Attendance Approval System

Effortlessly manage and approve student attendance requests with this user-friendly platform. Designed for convenience, the system bridges the communication gap between students and teachers, making attendance approval quick and efficient.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Student Dashboard](#student-dashboard)
  - [Admin Dashboard](#admin-dashboard)
- [Conclusion](#conclusion)

---

## Introduction

The **Student Attendance Approval System** is designed to resolve the challenges students face in seeking attendance permission during critical periods. By leveraging Python and SQL, this project provides a seamless interface for both students and admins to interact efficiently.

The core system is managed via `main.py`, which provides a GUI built using Tkinter. The application stores data in local text files and a SQLite database to ensure proper functionality. Users can access this system anytime and anywhere with an internet connection.

---

## Features

### Student Dashboard
1. **Make Request**:  
   Submit attendance requests by providing details like:
   - ID
   - Name
   - Branch
   - Dates (From and To)
   - Periods
   - Reason for absence

2. **View Request**:  
   Check the status of submitted attendance requests.

### Admin Dashboard
1. **Student Requests**:  
   View all attendance requests submitted by students and approve or reject them.
   
2. **Student Details**:  
   View the profiles and information of registered students.

---

## Technologies Used

- **Programming Language**: Python 3.12.0
- **GUI Framework**: Tkinter
- **Database**: SQLite3
- **File System**: Text files for specific data storage

---

## System Requirements

- Python 3.12.0 or higher
- SQLite3 (comes pre-installed with Python)
- Internet connection for remote access (optional)
- Compatible operating system: Windows, macOS, or Linux

---

## Installation

1. Clone this repository:
   ```bash
git clone https://github.com/satvikaj/Student-AttendanceApproval.git
   cd student-attendance-approval
