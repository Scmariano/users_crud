from msilib import schema
from flask_app.config.mysqlconnection import connectToMySQL


class User:
    schema = 'users_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL(cls.schema).query_db(query)
        users = []
        for i in results:
            users.append( cls(i) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s, NOW() , NOW());"
        return connectToMySQL(cls.schema).query_db(query,data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s"
        results = connectToMySQL(cls.schema).query_db(query, data)
        row = results[0]
        user = cls(row)
        return user

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s,  last_name = %(last_name)s,  email = %(email)s, created_at = NOW(), updated_at = NOW() WHERE id = %(id)s"
        return connectToMySQL(cls.schema).query_db(query,data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s"
        return connectToMySQL(cls.schema).query_db(query,data)