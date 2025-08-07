# Webshop User Management API

This is a RESTful API built with **FastAPI** to manage users and shopping carts for an online webshop. The application does not include a frontend, but provides backend functionality that could serve as the foundation for a complete e-commerce system.

All data is stored locally in a `data.json` file.

## Features

- **User Management**
  - Assign users to a shop
  - Retrieve information about a specific user
  - List all users

- **Shopping Cart Management**
  - Add a new cart for a given user
  - Insert products into the cart
  - Update or delete existing products in the cart
  - View the contents of a specific user's cart
  - Calculate the total price of products in a cart

## Example Use Cases

- Add a new user and assign them a cart
- Place multiple items in their cart
- Modify quantities or remove items
- Retrieve the cart’s contents and total cost
- Query all registered users or details of a specific one

## Technologies Used

- Python 3
- [FastAPI](https://fastapi.tiangolo.com/)
- JSON file for data persistence

## How to Run

1. Install dependencies: `pip install fastapi uvicorn`
2. Start the API server: `python -m uvicorn main:app --reload`
3. Access the interactive API docs in your web browser at `http://127.0.0.1:8000/docs`
