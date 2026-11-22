# 🛒 Mini Product Search and Sorting System

A Python-based mini product management system that stores product data in JSON and performs searching and sorting operations.

---

## 📁 Project Structure

```text
Mini-Product-System/
│
├── products.json
├── functions.py
├── main.py
└── README.md
```

---

## 📦 Product Data

Product information is stored in `products.json`.

Each product contains the following fields:

- **ID** – Unique product identifier
- **Name** – Product name
- **Price** – Product price

The project contains 15 different products.

---

## ✨ Features

- Display all products
- Sort products by price (ascending)
- Sort products by price (descending)
- Search products by name
- Search products by ID
- Find the cheapest product
- Find the most expensive product

---

## 🔍 Searching Algorithms

### Linear Search

Used to search for products by name.

- Checks elements one by one.
- Stops when the product is found.
- **Time Complexity:** `O(n)`

### Binary Search

Used to search for products by ID.

- Requires sorted data.
- Divides the search interval into halves.
- **Time Complexity:** `O(log n)`

---

## 🔄 Sorting Algorithm

### Bubble Sort

Used to sort products according to their prices.

- Ascending order
- Descending order
- Compares adjacent elements
- Swaps elements when necessary

**Time Complexity:**

| Case | Complexity |
|---|---|
| Best Case | O(n²) |
| Average Case | O(n²) |
| Worst Case | O(n²) |

---

## 🏆 Product Analysis

- `min()` – Finds the cheapest product.
- `max()` – Finds the most expensive product.

---

## 🛠️ Technologies

- Python
- JSON
- Git
- GitHub

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/Svetlana-Allahverdiyeva/MiniProductSearch-SortingSystem.git
```

Navigate to the project directory:

```bash
cd MiniProductSearch-SortingSystem
```

Run the program:

```bash
python main.py
```

---

## 🎯 Project Purpose

This project demonstrates the use of Python functions, JSON file handling, modular programming, searching algorithms, sorting algorithms, and version control using Git.