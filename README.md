# 🗃️ Inventory Management System

> **ITI ITP Django Course Project - Python Fullstack Group 2**

This is a **web-based inventory management system** built with Django and PostgreSQL to solve real-world problems for a local warehouse that supplies goods to supermarkets.  
It helps track incoming shipments from factories and outgoing orders to supermarkets, with role-based access for employees and managers.

---

## 🏢 Business Problem Statement

A local warehouse handles **huge amounts of products daily**. Managing shipments and orders manually has become overwhelming. The warehouse needs a **centralized system** to:

- Track shipments from factories.  
- Track orders to supermarkets.  
- Monitor product quantities in real-time.  
- Highlight critical stock levels for immediate action.

This system **excludes pricing or accounting features**, focusing only on inventory flow and user management.

---

## 🚀 Features

### 👨‍💼 Manager
- Full access to all system features.
- Can **add/edit employees** and provide them with credentials.
- **Modify** (but not delete) any order or shipment.
- Dedicated dashboard pages for:
  - **Pending Orders & Shipments** (approve/reject).
  - **Low Quantity Products** for critical inventory management.
- Filter records by name, status, or date.

### 👨‍🔧 Employee
- Login securely to their account.
- Dashboard with three main pages:
  - **Orders**: View all orders, add new orders.
  - **Shipments**: View all shipments, add new shipments.
  - **Inventory**: List of all products with pagination & search.
    - Products below critical stock are highlighted.
    - Products with 0 quantity have distinct highlighting.
- Can create new orders and shipments, pending manager approval.
- View status of their orders (Pending / Confirmed).

---

## 📦 Tech Stack

| Tech            | Details                |
|-----------------|------------------------|
| **Backend**     | Django 4.x             |
| **Database**    | PostgreSQL             |
| **Frontend**    | Django Templates + Tailwind CSS |
| **Deployment**  | PythonAnywhere          |
| **Version Control** | Git + GitHub        |

---

## 📂 Project Structure

project/
├── products/
│ ├── templates/products/
│ │ ├── employee_inventory.html
│ │ ├── manager_inventory.html
│ ├── models.py
│ ├── views.py
│ ├── urls.py
├── orders/
├── shipments/
├── users/
│ ├── templates/users/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
├── static/
│ ├── css/
│ ├── js/
│ └── images/
├── manage.py
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/EmadSayed650/Project-Django.git


