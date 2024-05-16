from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user, queries
db = "rideshares"
table = "messages"
class Message:
    def __init__(self,data) -> None:
        self.id = data["id"]
        self.content = data["content"]
        self.sender = None

    @classmethod
    def save(cls, data):
        query = queries.create_query(table, data)
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_messages_by_ride(cls, data):
        query = "SELECT * FROM messages LEFT JOIN rides ON rides.id = messages.rides_id JOIN users ON users.id = messages.users_id  WHERE rides.id = %(ride_id)s ORDER BY rides.created_at ASC;"
        results = connectToMySQL(db).query_db(query, data)
        all_messages = []

        if (results):
            for row in results:
                message = cls(row)

                sender_data = {
                    "id": row["users.id"],
                    "first_name": row["first_name"],
                    "last_name" : row["last_name"],
                    "email": row["email"],
                    "password": row["password"]
                }
                message.sender = user.User(sender_data)
                all_messages.append(message)
        return all_messages

