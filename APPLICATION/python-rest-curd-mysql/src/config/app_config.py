from flask import Flask, request, json, Response
from flask_restful import Resource
import logging as log
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root"
)

app = Flask(__name__)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE IF NOT EXISTS ESPARK")
my_cursor.execute(
    "CREATE TABLE IF NOT EXISTS ESPARK.USER_DATA "
    "(id INT AUTO_INCREMENT PRIMARY KEY, USER_NAME VARCHAR(255))")

empty_check_sql = "SELECT EXISTS(SELECT 1 FROM ESPARK.USER_DATA) AS RESPONSE"
insert_sql = "INSERT INTO ESPARK.USER_DATA (ID,USER_NAME) VALUES (%s,%s)"
select_all_sql = "SELECT * FROM ESPARK.USER_DATA"
select_by_id_sql = "SELECT * FROM ESPARK.USER_DATA WHERE ESPARK.USER_DATA.ID=$id"
update_sql = "UPDATE ESPARK.USER_DATA SET ESPARK.USER_DATA.USER_NAME='$name' WHERE ESPARK.USER_DATA.ID=$id"
delete_sql = "DELETE FROM ESPARK.USER_DATA WHERE ESPARK.USER_DATA.ID=$id"


class AppConfig:

    def __init__(self):
        log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')
        log.info('AppConfig Constructor ')
