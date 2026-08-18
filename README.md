# Inventory Management System

A Python-based console application for managing inventory items and tracking stock levels using Object-Oriented Programming (OOP).

## Overview

This project is a beginner-level inventory management system built with Python. It allows users to view available items, select an item, restock inventory, sell/remove stock, and check the current quantity.

The project was created to practice core Object-Oriented Programming concepts such as classes, objects, methods, encapsulation of object state, and composition.

## Features

* Add inventory items using unique item IDs
* Display available inventory items
* Restock items
* Sell/remove items from stock
* Check current item quantity
* Validate stock operations
* Prevent removing more stock than is available
* Handle invalid numeric input
* Store inventory items using a Python dictionary

## Technologies Used

* Python 3
* Object-Oriented Programming
* Python Dictionaries
* Exception Handling
* Input Validation

## OOP Structure

### `Item`

Represents an individual inventory item.

Each item contains:

* `name` — item name
* `price` — item price
* `quantity` — current stock quantity
* `item_id` — unique identifier

Methods:

* `add_stock(units)` — increases the available stock
* `remove_stock(units)` — decreases stock if sufficient quantity is available

### `Inventory`

Manages multiple `Item` objects.

The inventory stores items in a dictionary using their `item_id` as the key.

Methods:

* `add_item(item)` — adds an item to the inventory
* `menu()` — provides the interactive console interface

## Example Inventory

The current version starts with three sample products:

| Product | Price | Quantity | ID |
| ------- | ----: | -------: | -: |
| Chips   |    10 |       10 |  1 |
| Biscuit |    30 |       40 |  2 |
| Burger  |    69 |       15 |  3 |

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Krishna25-tech/Inventory-Management-System.git
```

### 2. Navigate to the project

```bash
cd Inventory-Management-System
```

### 3. Run the program

```bash
python inventory_management.py
```

## Example Operations

After starting the program, the available inventory is displayed.

The user can select an item and perform operations such as:

```text
1. Restock
2. Sell
3. Check quantity
4. Back to item list
```

The program validates the entered values and prevents invalid stock operations.

## Current Limitations

This is a learning project and is not intended to be a production inventory management system.

Current limitations include:

* Inventory data is not saved permanently
* Items are currently defined directly in the Python file
* No database is used
* No graphical user interface
* No authentication or user roles
* No sales history
* No automatic inventory reports

## Future Improvements

Possible improvements include:

* Add and remove items dynamically
* Add persistent storage using JSON or SQLite
* Add transaction/sales history
* Add low-stock alerts
* Add inventory reports
* Improve menu navigation
* Add a graphical user interface
* Separate the application into multiple modules
* Add automated tests

## Learning Goals

This project was built as part of my Python learning journey to strengthen:

* Object-Oriented Programming
* Classes and objects
* Methods
* Object composition
* Dictionaries
* Exception handling
* Input validation
* Git and GitHub workflow

## License

This project is licensed under the MIT License.
