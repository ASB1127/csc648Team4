from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
'''
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="mysqluser",
  password="password",
  database="topicmatchdb"
)
'''
'''
def get_profiles():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Profiles")
    result = cursor.fetchall()
    return {"employees": result}

def get_employee(id: int):
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM employees WHERE id = {id}")
    result = cursor.fetchone()
    return {"employee": result}
'''

app.mount("/static", StaticFiles(directory="/mydev/html/static"), name="static")


templates = Jinja2Templates(directory="/mydev/html/templates")


@app.get("/profile/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="profile.html", context={"id": id}
    )
