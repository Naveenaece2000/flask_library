from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize App
app = Flask(__name__)

# --- TIER 3: DATA LAYER CONFIGURATION ---
# We use SQLite for simplicity. It creates a file named 'library.db' automatically.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Database Model (The Schema)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# --- TIER 2: APPLICATION LAYER (LOGIC) ---

# Route 1: READ - Get all books and display them
@app.route('/')
def index():
    # Query Tier 3 to get all data
    all_books = Book.query.all()
    # Send data to Tier 1
    return render_template('index.html', books=all_books)

# Route 2: CREATE - Add a new book
@app.route('/add', methods=['POST'])
def add():
    # Get data from Tier 1 (Form)
    title = request.form.get('title')
    author = request.form.get('author')

    # Process Logic: Check if not empty
    if title and author:
        new_book = Book(title=title, author=author)
        # Save to Tier 3
        db.session.add(new_book)
        db.session.commit()
    
    return redirect(url_for('index'))

# Route 3: DELETE - Remove a book
@app.route('/delete/<int:id>')
def delete(id):
    # Find item in Tier 3
    book_to_delete = Book.query.get_or_404(id)
    
    # Delete from Tier 3
    db.session.delete(book_to_delete)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)