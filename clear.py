from tinydb import TinyDB

db = TinyDB("db.json")
db.truncate()
