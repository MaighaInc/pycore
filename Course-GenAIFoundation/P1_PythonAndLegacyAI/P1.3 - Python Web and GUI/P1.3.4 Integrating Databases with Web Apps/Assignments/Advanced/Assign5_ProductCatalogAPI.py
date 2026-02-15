"""
Assignment 5: Product Catalog REST API with Advanced Filtering (Advanced)

Scenario:
You are building an advanced RESTful API for your product catalog. The API supports filtering products by name or price range. It also includes endpoints for updating and deleting products, and returns detailed error messages.

Objective:
- Build REST API endpoints for CRUD operations with advanced filtering
- Accept and return JSON data
- Implement error handling and validation

Tasks:
1. Create Flask routes for the following endpoints:
   - GET /products: List products, with optional query parameters for name filter, min_price, max_price
   - POST /products: Add a new product (name, price)
   - PUT /products/<id>: Update a product's name or price
   - DELETE /products/<id>: Delete a product by id
2. Accept and return JSON for all endpoints.
3. Implement filtering by name (substring match) and price range.
4. Return appropriate error messages and status codes for invalid input or missing products.
5. No HTML forms or templates—API only.

Hints:
- Use Flask's jsonify and request.args/get_json()
- Use SQL WHERE for filtering
- Use proper HTTP status codes (200, 201, 400, 404)

Rubric:
- CRUD endpoints: 30%
- Filtering logic: 30%
- JSON handling and error messages: 25%
- Code clarity and comments: 15%
"""