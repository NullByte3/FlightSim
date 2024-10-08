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

# I don't know if this should be fixed, but the problem with this is that the player would never spawn on an airport in Antarctica, - NullByte3.
# This is very easy to fix, but fuck it.
def get_random_airport():
    cursor = db.cursor()
    cursor.execute("SELECT name, continent, latitude_deg, longitude_deg FROM airport WHERE type = 'large_airport' ORDER BY RAND() LIMIT 1")
    return cursor.fetchone()

# I included continent, so it's less confusing as we have get_random_airport() and that.
# - NullByte3
def get_airports_by_continent(continent):
    cursor = db.cursor()
    if continent == 'AN':
        cursor.execute("SELECT name, continent, latitude_deg, longitude_deg FROM airport WHERE continent = 'AN' ORDER BY RAND() LIMIT 8")
    else:
        cursor.execute("SELECT name, continent, latitude_deg, longitude_deg FROM airport WHERE continent = %s AND type = 'large_airport' ORDER BY RAND() LIMIT 8", (continent,))
    return cursor.fetchall()

def get_cost(airport_one, airport_two):
    return haversine(airport_one[3], airport_one[2], airport_two[3], airport_two[2]) * 0.12

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


def get_score(username):
    cursor = db.cursor()
    cursor.execute("SELECT score FROM users WHERE username = %s", (username,))
    return cursor.fetchone()[0]

def add_score(username, score):
    cursor = db.cursor()
    cursor.execute("UPDATE users SET score = score + %s WHERE username = %s", (score, username))
    db.commit()

def has_played_before(username):
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
    if cursor.fetchone()[0] > 0:
        return True
    else:
        cursor.execute("INSERT INTO users (username, score) VALUES (%s, 0)", (username,))
        db.commit()
        return False


def get_db():
    return db
