import psycopg
import time

while 1 :
    try :
        conn = psycopg.connect(host='localhost', dbname= 'shron', user='postgres', password='newpass')
        cursor = conn.cursor()
        print("Database connected successfully ")
        break
    except Exception as error :
        print( "Connection failed ")
        print( "ERROR : ",error)
    time.sleep(2)

