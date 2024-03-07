from fastapi import FastAPI
import logging
import mysql.connector

cnx = mysql.connector.connect(user='root', password='password',
                              host='db',
                              database='TopicMatch')
app = FastAPI()

# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__) 

logger.info("logging from the root logger")

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
            
