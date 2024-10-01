from dotenv import load_dotenv
load_dotenv()
import database
def tick():
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM country")
    result = cursor.fetchall()
    for row in result:
        print(row)
    print("tick")


tick();
