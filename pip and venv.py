import psycopg2 as psql
from psycopg2 import sql

class Database:
    @staticmethod
    def connect (query : str , query_type : str):
        db = psql.connect(
            database="test",
            user="postgres",
            password="davon",
            host="localhost",
            port="5432"

        )

        cursor = db.cursor()
        cursor.execute(query)
        data =["update","insert" ,"delete","alter"]
        if query_type in data :
            db.commit()
            if query_type == "update":
                return "updated data"
            elif query_type == "insert":
                return "inserted data"
            elif query_type == "delete":
                return "deleted data"
            elif query_type == "alter":
                return "altered data"
        else :
            return cursor.fetchall()





















