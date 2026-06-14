from pymongo import MongoClient


client = MongoClient("mongodb+srv://Trent:<db_password>@cluster0.dyq8pd3.mongodb.net/?appName=Cluster0")

db = client["books_db"]
books = db["books"]

# Очистка коллекции (необязательно)
books.delete_many({})

# Гра престолів
books.insert_one({
    "title": "Гра престолів",
    "price": 500,
    "year": 2022,
    "pages": 864
})

# Книги зі шкільних предметів
books.insert_many([
    {
        "title": "Математика",
        "class": 5,
        "year": 2022,
        "pages": 240
    },
    {
        "title": "Українська мова",
        "class": 6,
        "year": 2022,
        "pages": 280
    },
    {
        "title": "Історія України",
        "class": 7,
        "year": 2021,
        "pages": 320
    },
    {
        "title": "Географія",
        "class": 8,
        "year": 2022,
        "pages": 300
    },
    {
        "title": "Біологія",
        "class": 9,
        "year": 2022,
        "pages": 350
    }
])

print("=== Книги для 5-8 класів ===")
for book in books.find(
        {"class": {"$gte": 5, "$lte": 8}}
):
    print(book)

print("\n=== Книги 2022 року ===")
for book in books.find(
        {"year": 2022}
).sort("class", -1).limit(3):
    print(book)

print("\n=== Книга з найбільшою кількістю сторінок ===")
for book in books.find().sort("pages", -1).limit(1):
    print(book)