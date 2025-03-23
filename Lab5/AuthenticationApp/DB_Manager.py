import os
import sqlite3

class DatabaseManager:
    CREATE_AUTHENTICATION_TABLE_CMD='''create table if not exists authentication(
                                                                                id integer primary key autoincrement,
                                                                                email varchar(200) unique,
                                                                                username varchar(200) unique,
                                                                                password varchar(200) unique)'''

    CREATE_SCORES_TABLE_CMD='''create table if not exists scores(id integer primary key autoincrement,
                                                            user1_2 varchar(200) unique,
                                                            score varchar(200))'''

    INSERT_AUTHENTICATION_CMD='''insert into authentication(email,username,password) values (?,?,?)'''
    INSERT_SCORE_CMD='''insert into scores(user1,user2,score) values(?,?,?)'''

    GET_SCORE_BY_USERNAMES_CMD='''select score from scores where user1_2= ?'''

    GET_USERNAME_BY_PASSWORD='''select username from authentication where password= ?'''

    UPDATE_SCORE_WITH_USERNAMES_AND_NEW_SCORES_CMD='''update scores set score=? where user1_2=??'''

    CURRENT_PATH=os.path.dirname(os.path.abspath(__file__))
    DATABASE_PATH=os.path.join(CURRENT_PATH,'MainDB.db')

    def __init__(self,errorQueue):
        self.errorQueue=errorQueue
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.CREATE_AUTHENTICATION_TABLE_CMD)
            cursor.execute(self.CREATE_AUTHENTICATION_TABLE_CMD)
            cursor.close()

    def insertAuthenticationEntry(self,email:str,user:str,password:str):
        try:
            with sqlite3.connect(self.DATABASE_PATH) as db:
                cursor=db.cursor()
                cursor.execute(self.INSERT_AUTHENTICATION_CMD,(email,user,password))
        except sqlite3.IntegrityError as e:
            self.errorQueue.put("DB_ERROR.COULD_NOT_INSERT_AUTHENTICATION_ENTRY")
            raise Exception("Could Not Insert Authentication")
        finally:
            cursor.close()

    def insertScore(self,user1:str,user2:str,score:int):
        user1_2=user1+"_"+user2
        try:
            with sqlite3.connect(self.DATABASE_PATH) as db:
                cursor=db.cursor()
                cursor.execute(self.INSERT_SCORE_CMD,(user1_2,score))
        except sqlite3.IntegrityError as e:
            self.errorQueue.put("DB_ERROR.COULD_NOT_INSERT_SCORE")
        finally:
            cursor.close()

    def getScoreByUsernames(self,user1:str,user2:str):
        user1_2=user1+"_"+user2
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.GET_SCORE_BY_USERNAMES_CMD,(user1_2,))
            returnval=str(cursor.fetchone()[0])
            cursor.close()
            return returnval



    def getUsernameByPassword(self,password:str):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.GET_USERNAME_BY_PASSWORD,(password,))
            result=cursor.fetchone()
            cursor.close()

            if result:
                return str(result[0])
            self.errorQueue.put("DB_ERROR.USER_NOT_FOUND")
            raise Exception("User not found")



    def updateScoreWithUsernamesAndNewScore(self,score:str,user1:str,user2:str):
        user1_2=user1+"_"+user2
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.UPDATE_SCORE_WITH_USERNAMES_AND_NEW_SCORES_CMD,(score,user1_2))
            cursor.close()


