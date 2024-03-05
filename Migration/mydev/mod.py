from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import mysql.connector
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


app = FastAPI()

cnx = mysql.connector.connect(user='root', password='password',
                              host='tmysql',
                              database='topicmatchdb')

print(cnx)

app.mount("/static", StaticFiles(directory="/mydev/html/static"), name="static")


templates = Jinja2Templates(directory="/mydev/html/templates")


@app.get("/profile/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    log.info('help!')
    return templates.TemplateResponse(
        request=request, name="profile.html", context={"id": row[0]}
    )
