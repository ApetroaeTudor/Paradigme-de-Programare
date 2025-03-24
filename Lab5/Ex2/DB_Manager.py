import os
import sqlite3

class DatabaseManager:
    CREATE_AUTHENTICATION_TABLE_CMD='''create table if not exists authentication(
                                                                                id integer primary key autoincrement,
                                                                                email varchar(200) unique,
                                                                                username varchar(200) unique,
                                                                                password varchar(200) unique)'''






    CURRENT_PATH=os.path.dirname(os.path.abspath(__file__))
    DATABASE_PATH=os.path.join(CURRENT_PATH,'MainDB.db')

    def __init__(self,errorQueue):
        self.errorQueue=errorQueue
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.CREATE_AUTHENTICATION_TABLE_CMD)
            cursor.execute(self.CREATE_GAMES_TABLE_CMD)
            cursor.close()

    INSERT_AUTHENTICATION_CMD='''insert into authentication(email,username,password) values (?,?,?)'''
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

    GET_USERNAME_BY_PASSWORD='''select username from authentication where password= ?'''
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

    GET_ID_BY_NAME='''select id from authentication where username=?'''
    def getIDbyName(self,name:str):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.GET_ID_BY_NAME,(name,))
            result=cursor.fetchone()[0]
            cursor.close()
            return result

    CREATE_GAMES_TABLE_CMD = '''create table if not exists games (
                                                                       gameID integer primary key,
                                                                       player0ID integer not null,
                                                                       player1ID integer not null,
                                                                       player0Score integer,
                                                                       player1Score integer,
                                                                       check(player0ID<player1ID),
                                                                       unique(player0ID,player1ID));'''

    GET_SCORES_BY_PLAYER_IDS_CMD='''select player0Score, player1Score from games where player0ID=? and player1ID=?'''
    def getScoresByPlayerIDS(self,id1:int,id2:int):
        if id1>id2:
            id1,id2=id2,id1
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.GET_SCORES_BY_PLAYER_IDS_CMD,(id1,id2))
            result=cursor.fetchone()
            cursor.close()
            return result

    INIT_GAME_CMD='''insert into games(player0ID,player1ID,player0Score,player1Score) values(?,?,0,0)'''
    def initGameWithUserIDS(self,id1:int,id2:int):
        if id1>id2:
            id1,id2=id2,id1
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.INIT_GAME_CMD,(id1,id2))
            cursor.close()

    INCREMENT_PLAYER0_SCORE_CMD='''update games set player0Score = player0Score +1 where player0ID=? and player1ID=?'''
    INCREMENT_PLAYER1_SCORE_CMD='''update games set player1Score = player1Score +1 where player0ID=? and player1ID=?'''

    def incrementPlayer0Score(self,player0ID:int,player1ID:int):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.INCREMENT_PLAYER0_SCORE_CMD,(player0ID,player1ID))
            cursor.close()

    def incrementPlayer1Score(self,player0ID:int,player1ID:int):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor=db.cursor()
            cursor.execute(self.INCREMENT_PLAYER1_SCORE_CMD,(player0ID,player1ID))
            cursor.close()







