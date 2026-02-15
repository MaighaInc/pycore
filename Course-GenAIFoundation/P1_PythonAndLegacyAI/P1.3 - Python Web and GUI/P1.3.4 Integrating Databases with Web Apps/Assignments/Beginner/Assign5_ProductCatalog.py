"""
Assignment 5: Product Catalog REST API - Add and List (Beginner)

Scenario:
You are building a simple RESTful API for your product catalog. The API allows clients to add and list products using JSON requests and responses.

Objective:
- Build REST API endpoints for basic product operations
- Accept and return JSON data
- No HTML forms or templates—API only

Tasks:
1. Create a Flask app and connect it to a SQLite database called 'products.db'.
2. Create a table 'products' with columns: id (INTEGER PRIMARY KEY), name (TEXT), price (REAL).
3. Create Flask routes for the following endpoints:
   - GET /products: List all products
   - POST /products: Add a new product (name, price)
4. Accept and return JSON for all endpoints.
5. Return appropriate error messages and status codes for invalid input.
6. No HTML forms or templates—API only.

Hints:
- Use Flask's jsonify and request.get_json()
- Use proper HTTP status codes (200, 201, 400)
- Use sqlite3 for database operations

Rubric:
- Endpoints: 40%
- JSON handling: 30%
- Error handling: 20%
- Code clarity and comments: 10%
"""