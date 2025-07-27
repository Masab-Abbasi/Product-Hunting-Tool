# 🛒 Product Hunting Tool

**Product Hunting Tool** is a powerful console-based application designed for **business owners, entrepreneurs, and sellers** who want to analyze the performance of products before launching them into the market. This tool helps you make data-driven decisions by allowing you to search products and view key performance indicators like ratings, monthly sales, and smart recommendations.

---

## 📌 Features

- 🔐 **Secure User and Admin Login System**
- ✅ **Strong Password Validation**
- 📁 **Category-Wise Product Management (8 Categories)**
- 🔍 **Smart Product Search (Partial Match)**
- ⭐ **View Product Ratings, Sales, and AI-Based Recommendations**
- 🛠️ **Admin Panel to Edit/Add Products**
- 📄 **File-Based Data Storage (No Database Required)**

---

## 🧩 Key Concepts Used

- **File Handling** (`open`, `read`, `write`, `append`)
- **Modular Programming** (organized with functions per feature)
- **Exception Handling** (`try-except` for robust input & file error checks)
- **Input Validation** (`isalpha()`, `isdigit()`, `isalnum()`)
- **String Manipulation** (`split`, `strip`, `lower`)
- **Global Variables** (for session tracking)
- **Loops & Conditional Logic** (`while`, `if-elif-else`)

---

## 🗂️ Category List

- Home and Kitchen  
- Health and Personal Care  
- Electronics  
- Toys and Games  
- Beauty and Personal Care  
- Clothing, Shoes and Jewelry  
- Sports and Outdoors  
- Pet Supplies  

Each category has its own `.txt` file (e.g., `Home and Kitchen.txt`) storing product data in this format:


---

## 🔑 Security Features

- ✅ **Strong Password Check:** Minimum 8 characters, at least 1 digit, 1 uppercase, and 1 special character.
- 🚫 **Duplicate Username Prevention**
- 🔐 **Admin Access Protection** using a fixed secret password.
- 💥 **Login Attempt Limits** (3 attempts)

---

## 🧠 Smart Recommendation Engine

The tool provides recommendations based on:

- ⭐ **Ratings**
- 📈 **Monthly Sales**

Sample logic:
- Rating ≥ 4.5 and Sales ≥ 1500 → **"Highly Recommended Product"**
- Rating ≥ 4.0 and Sales ≥ 1000 → **"Good Product"**
- Else → **"Not Recommended"**

---

## 👤 User Flow

1. **Login/Register**
2. **Select a Category**
3. **Search Product by Name (Partial Search Allowed)**
4. **View Ratings, Sales, or Get Recommendation**
5. **Continue Search / Go to Main Menu / Exit**

---

## 🔧 Admin Panel

Admins can:
- 🔄 **Edit Existing Categories**
- 🆕 **Add More Products**
- 📝 **Write Data to Category Files**

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- A code editor (VS Code / PyCharm recommended)

### To Run:
```bash
python product_hunting_tool.py
