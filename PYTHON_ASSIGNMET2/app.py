from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = 'bookbuddy.db'

# Helper function to connect to the database
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Validation function
def validate_book_data(data):
    genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Sci-Fi']
    if not data.get('title') or not data.get('author') or not data.get('published_year') or not data.get('genre'):
        return False, "Missing required fields"
    if not isinstance(data['published_year'], int) or not (1000 <= data['published_year'] <= datetime.now().year):
        return False, "Invalid year"
    if data['genre'] not in genres:
        return False, "Invalid genre"
    return True, ""

@app.route('/')
def home():
    return "Welcome to BuddyBook"


# 1. POST: Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    is_valid, message = validate_book_data(data)
    
    if not is_valid:
        return jsonify({"error": "Invalid data", "message": message}), 400
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO books (title, author, published_year, genre)
    VALUES (?, ?, ?, ?)
    ''', (data['title'], data['author'], data['published_year'], data['genre']))
    
    conn.commit()
    book_id = cursor.lastrowid
    conn.close()
    
    return jsonify({"message": "Book added successfully", "book_id": book_id}), 201

# 2. GET: Retrieve all books
@app.route('/books', methods=['GET'])
def get_books():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    
    result = []
    for book in books:
        result.append(dict(book))
    return jsonify(result)

# 3. GET: Retrieve a specific book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id = ?', (id,))
    book = cursor.fetchone()
    conn.close()
    
    if book is None:
        return jsonify({"error": "Book not found", "message": "No book exists with the provided ID"}), 404
    
    return jsonify(dict(book))

# 4. PUT: Update an existing book's details
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    is_valid, message = validate_book_data(data)
    
    if not is_valid:
        return jsonify({"error": "Invalid data", "message": message}), 400
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE books SET title = ?, author = ?, published_year = ?, genre = ?
    WHERE id = ?
    ''', (data['title'], data['author'], data['published_year'], data['genre'], id))
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Book not found", "message": "No book exists with the provided ID"}), 404
    
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Book updated successfully"})

# 5. DELETE: Delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (id,))
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Book not found", "message": "No book exists with the provided ID"}), 404
    
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Book deleted successfully"})

# 6. Filter: Retrieve books by genre or author
@app.route('/books/filter', methods=['GET'])
def filter_books():
    genre = request.args.get('genre')
    author = request.args.get('author')
    
    query = 'SELECT * FROM books WHERE 1=1'
    params = []
    
    if genre:
        query += ' AND genre = ?'
        params.append(genre)
    if author:
        query += ' AND author = ?'
        params.append(author)
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(query, tuple(params))
    books = cursor.fetchall()
    conn.close()
    
    result = []
    for book in books:
        result.append(dict(book))
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
