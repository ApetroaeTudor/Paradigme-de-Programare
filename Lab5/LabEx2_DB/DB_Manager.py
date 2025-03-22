import sqlite3
import os

class DB_Manager:
    CREATE_ENTRIES_CMD='''create table if not exists entries(
                id integer primary key autoincrement,
                title varchar(100),
                content varchar(500)
                )'''
    CREATE_QUOTES_CMD='''create table if not exists quotes(
                id integer primary key autoincrement,
                content varchar(500)
                )'''
    SELECT_ENTRY_BY_TITLE_CMD='''select * from entries where title=?'''
    SELECT_ENTRY_BY_ID_CMD='''select * from entries where id=?'''
    SELECT_QUOTE_BY_ID_CMD='''select * from quotes where id=?'''
    INSERT_ENTRY_CMD='''insert into entries (title,content)
                    values(?,?)'''
    GET_ALL_ENTRY_NAMES_CMD='''select title from entries'''
    INSERT_QUOTE_CMD='''insert into quotes (content) values (?)'''
    UPDATE_ENTRY_BY_ID_CMD='''update entries set title=?,content=? where id=?'''

    DELETE_ENTRY_BY_NAME_CMD='''delete from entries where title=?'''

    SELECT_ENTRY_CONTENT_BY_NAME='''select content from entries where title=?'''

    GET_NR_OF_ENTRIES_CMD='''select count(*) from entries'''
    GET_NR_OF_QUOTES_CMD='''select count(*) from quotes'''

    CURRENT_PATH=os.path.dirname(os.path.abspath(__file__))
    DATABASE_PATH=os.path.join(CURRENT_PATH,'journal.db')

    def __init__(self):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.CREATE_ENTRIES_CMD)
            cursor.execute(self.CREATE_QUOTES_CMD)
            cursor.close()
    def insertEntry(self,title:str,content:str):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.INSERT_ENTRY_CMD,(title,content))
            cursor.close()
    def getEntryById(self,id:int):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.SELECT_ENTRY_BY_ID_CMD,(id,))
            rows=cursor.fetchall()
            cursor.close()
            myList= []
            for row in rows:
                myList[0]=row[1]
                myList[1]=row[2]
            return myList

    def insertQuote(self,content:str):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.INSERT_QUOTE_CMD,(content,))
            cursor.close()
    def getQuoteById(self,id:int):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.SELECT_QUOTE_BY_ID_CMD,(id,))
            rows=cursor.fetchall()
            returnval=""
            for row in rows:
                returnval=row[1]
            return returnval

    def getNrOfQuotes(self):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.GET_NR_OF_QUOTES_CMD)
            returnval = int(cursor.fetchone()[0])
            cursor.close()
            return returnval

    def getNrOfEntries(self):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.GET_NR_OF_ENTRIES_CMD)
            returnval=int(cursor.fetchone()[0])
            cursor.close()
            return returnval

    def getAllEntryNames(self):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.GET_ALL_ENTRY_NAMES_CMD)
            result=cursor.fetchall()
            myList=[]
            for elem in result:
                myList.append(str(elem[0]))
            cursor.close()
            return myList

    def selectEntryContentByName(self, name:str):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.SELECT_ENTRY_CONTENT_BY_NAME,(name,))
            returnval=cursor.fetchone()[0]
            cursor.close()
            return returnval

    def deleteEntryByName(self,name:str):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.DELETE_ENTRY_BY_NAME_CMD,(name,))
            cursor.close()


