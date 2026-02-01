from datetime import datetime
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")

bundle = joblib.load("./models/prix_m2_model.pkl")
model = bundle["model"] if isinstance(bundle, dict) else bundle

FEATURES = bundle.get("features", ["Surface reelle bati", "Nombre pieces principales", "arrondissement"]) if isinstance(bundle, dict) else \
           ["Surface reelle bati", "Nombre pieces principales", "arrondissement"]

MODEL_R2 = 0.19  # mets ton score actuel

def ctx(request: Request, **kwargs):
    base = {
        "request": request,
        "year": datetime.now().year,
        "model_name": type(model).__name__,
        "model_r2": MODEL_R2,
        "features": FEATURES,
    }
    base.update(kwargs)
    return base

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", ctx(request))

@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse("about.html", ctx(request))

@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    surface: float = Form(...),
    pieces: int = Form(...),
    arrondissement: int = Form(...)
):
    X = np.array([[surface, pieces, arrondissement]], dtype=float)
    pred_log = model.predict(X)
    prix_m2 = float(np.exp(pred_log)[0])
    prix_total = float(prix_m2 * surface)

    return templates.TemplateResponse(
        "result.html",
        ctx(
            request,
            surface=surface,
            pieces=pieces,
            arrondissement=arrondissement,
            prix_m2=round(prix_m2, 2),
            prix_total=round(prix_total, 2),
        )
    )