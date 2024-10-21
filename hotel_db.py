import sqlite3
from langchain_core.tools import tool

db = 'hotel.db'

@tool
def search_hotels(
    city: str = '',
    price: float = 0,
    rating: float = 0,
    name: str = ''
) -> list[dict]:
    """
    Searches for hotels based on the provided information.

    Args:
        city: The city where you want to find hotels.
        name: The name of the hotel (optional).
        rating: The desired hotel rating (optional).
        price: The desired upper price limit for the hotel (optional).

    Returns:
        list[dict]: A list of hotel dictionaries matching the search criteria.
    """
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    query = "SELECT * FROM hotels WHERE 1=1"
    params = []

    if city:
        query += " AND City LIKE ?"
        params.append(f"%{city}%")
    if name:
        query += " AND Hotel_Name LIKE ?"
        params.append(f"%{name}%")
    if price:
        query += " AND Hotel_Price <= ?"
        params.append(f"{price}")
    if rating:
        query += " AND Hotel_Rating >= ?"
        params.append(f"{rating}")
    cursor.execute(query, params)
    results = cursor.fetchall()

    conn.close()

    return [
        dict(zip([column[0] for column in cursor.description], row)) for row in results
    ]