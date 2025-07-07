import sqlite3
import argparse
from mcp.server.fastmcp import FastMCP

# Create FastMCP instance
mcp = FastMCP('sqlite-book-library')

def init_db():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            genre TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn, cursor

@mcp.tool()
def add_book(query: str) -> bool:
    """Add a new book to the library using a SQL INSERT query.

    Args:
        query (str): SQL query like:
            INSERT INTO books (title, author, year, genre)
            VALUES ('1984', 'George Orwell', 1949, 'Dystopian')

    Returns:
        bool: True if added successfully, False otherwise
    """
    conn, cursor = init_db()
    try:
        cursor.execute(query)
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error adding book: {e}")
        return False
    finally:
        conn.close()

@mcp.tool()
def get_books(query: str = "SELECT * FROM books") -> list:
    """Fetch books using a SQL SELECT query.

    Args:
        query (str): SQL SELECT query to retrieve books.

    Returns:
        list: List of tuples with book records
    """
    conn, cursor = init_db()
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching books: {e}")
        return []
    finally:
        conn.close()
@mcp.tool()
def delete_book(query: str) -> bool:
    """Delete a book using a SQL DELETE query.

    Args:
        query (str): SQL DELETE query like:
            DELETE FROM books WHERE id = 1

    Returns:
        bool: True if deletion was successful, False otherwise
    """
    conn, cursor = init_db()
    try:
        cursor.execute(query)
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error deleting book: {e}")
        return False
    finally:
        conn.close()

@mcp.tool()
def update_book(query: str) -> bool:
    """Update book information using a SQL UPDATE query.

    Args:
        query (str): SQL UPDATE query like:
            UPDATE books SET genre = 'Science Fiction' WHERE title = '1984'

    Returns:
        bool: True if update was successful, False otherwise
    """
    conn, cursor = init_db()
    try:
        cursor.execute(query)
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error updating book: {e}")
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    print("📚 Starting Book Library MCP server...")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--server_type", type=str, default="sse", choices=["sse", "stdio"]
    )

    args = parser.parse_args()
    mcp.run(args.server_type)
