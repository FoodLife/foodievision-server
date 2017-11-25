from flask import Flask
from flaskext.mysql import MySQL

class foodie_db:
    @staticmethod
    def login(connection,user_name,password):

        try:
            cur = connection.cursor()
            string = "call login('{}','{}') ".format(user_name,password)
            cur.execute(string)
            result = cur.fetchall()
            if result:
                return result[0][0]
            return -1
        except:
            return "exception"
    @staticmethod
    def logout(connection,user_token):
        cur = connection.cursor()
        string = "Call logout('{}')".format(user_token)
        cur.execute(string)
        result = cur.fetchall()
        if result:
            return result[0][0]
        return -2

    @staticmethod
    def create_user(connection,user_name,password):
        try:
            cur = connection.cursor()
            string = "call create_user('{}','{}') ".format(user_name,password)
            cur.execute(string)
            result = cur.fetchall()
            if result:
                return result[0][0]
            return -1
        except:
            return "exception"

    @staticmethod
    def create_picture(connection, user_token,analysis,confidence,is_food):
        try:
            cur = connection.cursor()
            string = "call create_picture('{}','{}','{}','{}')".format(user_token,analysis,confidence,is_food)
            cur.execute(string)
            result = cur.fetchall()

            if result[0]:
                return result[0]

        except:
            return "exception"

    @staticmethod
    def create_favorite(connection,user_token,picture_id):
        try:
            cur = connection.cursor()
            string = "call create_favorite('{}','{}')".format(user_token,picture_id)
            cur.execute(string)
            return cur.fetchall()
        except:
            return "exception"

    @staticmethod
    def delete_favorite(connection,user_token,picture_id):
        try:
            cur = connection.cursor()
            string = "call delete_favorite('{}','{}')".format(user_token,picture_id)
            cur.execute(string)
            return cur.fetchall()
        except:
            return "exception"

    @staticmethod
    def change_password(connection,user_token,new_password):
        try:
            cur = connection.cursor()
            string = "call change_password('{}','{}')".format(user_token,new_password)
            cur.execute(string)
            return cur.fetchall()
        except:
            return "exception"

