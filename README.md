# 🛒 Product Hunting Tool

**Product Hunting Tool** is a powerful **console-based Python application** designed for **business owners, entrepreneurs, and sellers** who want to analyze the performance of products before launching them into the market.

This tool helps you make **data-driven decisions** by providing insights like ratings, sales, and AI-style recommendations based on performance.

---

## 🎯 Purpose

> Designed during the ICT course project, this tool helps businesses identify winning products in specific categories based on existing market performance indicators like **ratings** and **monthly sales**.

---

## 📌 Features

- 🔐 **Secure User and Admin Login System**
- ✅ **Strong Password Validation**
- 📁 **Category-Wise Product Management (8 Categories)**
- 🔍 **Smart Product Search (Partial Match)**
- ⭐ **View Product Ratings, Sales, and Smart Recommendations**
- 🛠️ **Admin Panel to Edit/Add Products**
- 🗂️ **File-Based Data Storage (No Database Required)**

---

## 🧩 Key Concepts Used

- **File Handling** (`open`, `read`, `write`, `append`)
- **Modular Programming** (organized into reusable functions)
- **Exception Handling** (`try-except` for robust error control)
- **Input Validation** (`isalpha()`, `isdigit()`, `isalnum()`)
- **String Manipulation** (`split`, `strip`, `lower`)
- **Global Variables** (for login/session management)
- **Loops & Conditional Logic** (`while`, `if-elif-else`)

---

## 🗂️ Categories Covered

Each product falls under one of the following real-world domains, with each category having its own `.txt` file:

- 🏠 Home and Kitchen  
- 🧼 Health and Personal Care  
- 💻 Electronics  
- 🧸 Toys and Games  
- 💄 Beauty and Personal Care  
- 👗 Clothing, Shoes and Jewelry  
- 🏀 Sports and Outdoors  
- 🐾 Pet Supplies  

Example product data stored in:
Home and Kitchen.txt:
Electric Kettle 1.5L | 4.6 | 1800
Dish Rack Stainless Steel | 4.5 | 1500


---

## 🔐 Security Features

- ✅ **Strong Password Check:** Min 8 chars, includes uppercase, digit, and special char.
- 🚫 **Duplicate Username Detection**
- 🔐 **Admin Access Restriction** using a secure, fixed password.
- 💥 **Login Attempt Limits** (3 max retries)

---

## 🧠 Smart Recommendation Engine

Based on:
- ⭐ Product Ratings
- 📈 Monthly Sales

**Recommendation Logic**:
| Rating      | Sales      | Recommendation               |
|-------------|------------|------------------------------|
| ≥ 4.5       | ≥ 1500     | **Highly Recommended**       |
| ≥ 4.0       | ≥ 1000     | Good Product (Consider More) |
| Else        | Any        | Not Recommended              |

---

## 👤 User Flow

1. **Register/Login**
2. **Select a Category**
3. **Search for a Product**
4. **View Details / Recommendation**
5. **Repeat Search / Return to Main / Exit**

---

## 🔧 Admin Panel Features

- 🆕 Add new products to any category
- 🔄 Edit categories using simple input
- ✅ All changes reflect in corresponding `.txt` files

---

## 📘 Methods Overview

| **Method Name**            | **Purpose / Description**                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------|
| `register_user()`          | Handles user registration with strong password checks and duplicate detection.             |
| `login_user()`             | Verifies registered users with limited login attempts.                                     |
| `login_admin()`            | Validates admin credentials to access admin-only functionality.                            |
| `show_user_login_menu()`   | Menu to choose between register/login for regular users.                                   |
| `show_admin_menu()`        | Displays admin dashboard with editing options.                                             |
| `categoires()`             | Shows a list of product categories and stores the selected one.                            |
| `view_category(category)`  | Displays selected category and initiates product search.                                   |
| `search_products(filename)`| Lets user search by keyword and view rating, sales, and recommendation.                    |
| `choice_menu()`            | Post-search menu to search again, go home, or exit.                                        |
| `is_strong(password)`      | Validates password strength criteria.                                                      |
| `duplicate_user(username)` | Checks for existing usernames in the registration file.                                    |
| `edit_category()`          | Allows admin to append new product entries into category files.                            |

---

## 🚀 Getting Started

### 🔧 Prerequisites
- Python 3.x
- VS Code / PyCharm

### ▶️ Run the Program
```bash
python product_hunting_tool.py
