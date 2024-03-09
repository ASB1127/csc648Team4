from fastapi import FastAPI, Form
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from typing import Annotated
import logging
import mysql.connector

app = FastAPI()

app.mount("/static", StaticFiles(directory="./html/static"), name="static")
# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__) 

logger.info("logging from the root logger")



cnx = mysql.connector.connect(user='root', password='password',
                              host='db',
                              database='TopicMatch')


class Msg(BaseModel):
    toUser: int
    fromUser: int
    msg: str
    
    
@app.post("/process/message")
async def process_message(toUser: Annotated[int,Form()],fromUser:Annotated[int,Form()],msg: Annotated[str,Form()]):
    logger.info("Msg")
    return {
        "msg":msg
    }
    

@app.get("/")
async def root():
    logger.info("logging from the root logger")
    cursor = cnx.cursor()
    query = ("SELECT firstname, lastname FROM Users")
    cursor.execute(query)
    for (firstname, lastname) in cursor:
        logger.info("firstname="+firstname+" lastname="+lastname)
    return {"message": "Hello World"}


@app.get("/send/message/{fromUser}/{toUser}/{msg}")
async def sendMessage(fromUser,toUser,msg):
    cursor = cnx.cursor()
    query = ("INSERT INTO Message (mid, fromUser, toUser, msg) values(1, %s, %s, %s)")
    cursor.execute(query, (fromUser,toUser,msg))
    cnx.commit()
    cursor.close()
    return {"message":"message sent"}


@app.get("/receive/message/{fromUser}")
async def receiveMessage(fromUser:int):
    cursor = cnx.cursor()
    query = "SELECT mID, msg FROM  Message WHERE fromUser=%s"
    cursor.execute(query, [fromUser])
    msgEntry=cursor.fetchone()
    logger.info(msgEntry)
    cursor.close()
    return {"mID":msgEntry[0],"msg":msgEntry[1]}
            

