import mysql.connector
import os
from math import radians, cos, sin, asin, sqrt

db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def get_airports_by_continent(db, continent):
    cursor = db.cursor()
    if continent == 'AN':
        cursor.execute("SELECT name, latitude_deg, longitude_deg FROM airport WHERE continent = 'AN' ORDER BY RAND() LIMIT 5")
    else:
        cursor.execute("SELECT name, latitude_deg, longitude_deg FROM airport WHERE continent = %s AND type = 'large_airport' ORDER BY RAND() LIMIT 5", (continent,))
    return cursor.fetchall()

# haversine formula to calculate distance between two GPS points
# Read more at: https://en.wikipedia.org/wiki/Haversine_formula
# - NullByte3
def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r

def get_db():
    return db
