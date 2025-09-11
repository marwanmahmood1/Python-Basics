# 🐍 Python Basics

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)  

A structured beginner-to-intermediate roadmap for learning Python.  
This repo covers **fundamental concepts, practical examples, and projects** to build a strong foundation in Python programming.  

---

## 📖 Learning Path  

### 1. Introduction  
- [x] Hello World  
- [x] Comments  
- [x] Variables & Data Types  
- [x] Type Casting  
- [x] User Input  
- [x] Arithmetic Operators  

### 2. Control Flow  
- [x] If Statements  
- [x] Logical Operators  
- [x] While Loops  
- [x] For Loops  
- [x] Nested Loops  
- [x] Break & Continue  

### 3. Functions & Scope  
- [x] Defining Functions  
- [x] Return Statements  
- [x] Keyword Arguments  
- [x] Nested Functions  
- [x] Scope  

### 4. Data Structures  
- [x] Strings  
- [x] Lists
- [x] 2D Lists
- [x] Tuples
- [x] Sets
- [x] Dictionaries  

### 5. Modules & Packages  
- [x] Math Functions  
- [x] Importing Modules  
- [x] Built-in Modules (`math`, `random`, `datetime`)
- [x] Creating Modules & Packages

### 6. File Handling  
- [x] Reading Files  
- [x] Writing Files  
- [x] Using `with` Statement  

### 7. Error Handling  
- [x] Try/Except  
- [x] Else & Finally  
- [x] Raising Exceptions  
- [x] Custom Exceptions  

### 8. Object-Oriented Programming (OOP)  
- [x] Classes & Objects
- [x] Attributes & Methods
- [x] Inheritance
- [x] Encapsulation
- [x] Polymorphism

### 9. Projects  
- [x] **Project 1: Password Strength Checker** (Loops + Conditionals + Functions)  
- [x] **Project 2: Text Adventure Game** (Loops + Functions + OOP)  
- [x] **Project 3: Expense Tracker** (File Handling + Dictionaries)  

---

## 🛠️ Project Details  

### 🛡️ Project 1 – Password Strength Checker  
A beginner-friendly CLI application that evaluates password strength based on:  
- Length  
- Uppercase & lowercase letters  
- Numbers  
- Special characters  

It also checks against a small list of common weak passwords and provides feedback for improvement.  


## 🎮 Project 2 – Text Adventure Game

This project is a simple text-based adventure game.  
- The player navigates through different rooms, makes choices, and can collect items in their inventory.  
- It’s designed to teach you about **functions, conditionals, loops, and basic game logic** in Python.

### Improving The Game
This project is designed as a base you can build on. Some ideas:

1. **More Choices** – Add new locations (forest, cave, river) with unique outcomes.  
2. **Enemies** – Create an `Enemy` class and add simple combat (attack, defend, health).  
3. **Items & Inventory** – Expand the inventory with potions, weapons, and keys. Items can heal or unlock new areas.  
4. **Branching Storylines** – Choices can impact the story’s direction and endings. Example: helping an NPC may reward you later.  
5. **Win/Loss Conditions** – Define victory by reaching treasure or defeating a final boss, and defeat by losing all health.  


## 🏆 Project 3 – Personal Expense Tracker

This project demonstrates how to build a **practical Python application** that saves and retrieves user data. It combines key programming concepts you’ve learned throughout the course:

1. **File Handling** – Reading and writing expenses to a file ensures that data persists between sessions.  
2. **Functions** – The program is broken into smaller functions (`add_expense`, `view_expenses`, `save_expenses`) to make the code organized and reusable.  
3. **Data Structures** – Expenses are stored as a **list of tuples** `(amount, category)` for easy management.  
4. **Error Handling** – Input validation (like checking if the amount is a number) prevents program crashes.  
5. **User Interaction** – A simple text menu makes the program interactive and user-friendly.  

By completing this project, you practice **real-world coding skills** while applying the fundamentals of Python in a way that directly solves a problem people face in daily life.


### Improving The Program
Once you master the basics, you can **expand this project** with new features:

- Add **date tracking** for each expense.  
- Show **monthly or weekly totals** with summaries.  
- Categorize expenses with charts using `matplotlib`.  
- Export data to **CSV or JSON files** for external use.  
- Add a **search function** to filter by category or amount.  
- Create a simple **GUI (Graphical User Interface)** with `tkinter` or `PyQt`.  

These improvements will not only make your tracker more powerful, but also help you practice **intermediate Python skills** step by step.

---


## ▶️ How to Run  

To run any Python file in this repository:  

1. Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).  
2. Open a terminal (Command Prompt, PowerShell, or your IDE's terminal).  
3. Navigate to the directory containing the file.  
4. Run the script using:  

```bash
python 01_Hello_World.py
