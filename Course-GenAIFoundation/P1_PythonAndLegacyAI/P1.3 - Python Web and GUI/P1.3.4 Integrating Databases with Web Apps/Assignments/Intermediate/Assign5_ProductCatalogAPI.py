"""
Assignment 5: Product Catalog REST API - Add, List, Update, Delete (Intermediate)

Scenario:
You are extending your RESTful API for the product catalog. In addition to adding and listing products, clients can now update and delete products using JSON requests and responses.

Objective:
- Add, list, update, and delete products via REST API using Flask and SQLite
- Accept and return JSON data
- No HTML forms or templates—API only

Tasks:
1. Create Flask routes for the following endpoints:
   - GET /products: List all products
   - POST /products: Add a new product (name, price)
   - PUT /products/<id>: Update a product's name or price
   - DELETE /products/<id>: Delete a product by id
2. Accept and return JSON for all endpoints.
3. Return appropriate error messages and status codes for invalid input or missing products.

Hints:
- Use Flask's jsonify and request.get_json()
- Use proper HTTP status codes (200, 201, 400, 404)
- Use sqlite3 for database operations

Rubric:
- CRUD endpoints: 40%
- JSON handling: 40%
- Code clarity and comments: 20%
"""