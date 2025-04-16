# 🎓 Student Management System

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple command-line based **Student Management System** built with Python.  
Easily add students, assign grades, calculate averages, and view all student records.  
Data is stored persistently using JSON files.

---

## 📂 Features

- ✅ Add new students with unique IDs
- ✅ Enter grades for 6 core subjects
- ✅ Automatically calculate average grades
- ✅ Display all students with their grades and averages
- ✅ Persistent data storage using JSON

---

## 🚀 Getting Started

### 📌 Prerequisites

- Python 3.x installed
- No external libraries required

### 💻 Run the App

```bash
git clone https://github.com/your-username/student-management-system.git
cd student-management-system
python student_manager.py
```

💾 JSON Data Format Example
{
"1": {
"name": "Jane Doe",
"grades": {
"Math": 17,
"English": 15,
"French": 16,
"Physics": 18,
"Chemistry": 14,
"Biology": 19
},
"average": 16.5
}
}

📁 Project Structure
student-management-system/
├── student_manager.py # Main Python script
├── students.json # Stores student data
└── README.md # Project documentation

✨ Future Improvements
GUI version using Tkinter or PyQt

Subject customisation

Search by ID or partial name

Grade reports export (PDF/CSV)
