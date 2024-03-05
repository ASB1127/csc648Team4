from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path



app = FastAPI()


app.mount("/static", StaticFiles(directory="/mydev/html/static"), name="webPageImgs")


templates = Jinja2Templates(directory="/mydev/html/templates")


@app.get("/profile/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="profile.html", context={"id": id}
    )

