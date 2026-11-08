from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR / "public"

app = FastAPI()

app.mount(
    "/public",
    StaticFiles(directory=PUBLIC_DIR),
    name="public",
)

templates = Jinja2Templates(directory=BASE_DIR / "templates")

IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".gif",
    ".webp", ".bmp", ".avif"
}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    photos = sorted(
        file.name
        for file in PUBLIC_DIR.iterdir()
        if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS
    )

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"photos": photos},
    )