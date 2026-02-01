from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import numpy as np

MODEL_PATH = "models/prix_m2_model.pkl"

app = FastAPI()
templates = Jinja2Templates(directory="templates")
data = joblib.load(MODEL_PATH)
model = data["model"] if isinstance(data, dict) else data

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request":request}
    )

@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    surface: float = Form(...),
    pieces: int = Form(...),
    arrondissement: int = Form(...)
):
    x = np.array([[surface, pieces, arrondissement]], dtype=float)
    pred_log = model.predict(x)
    prix_m2 = float(np.exp(pred_log)[0])
    prix_total = prix_m2 * surface

    return templates.TemplateResponse(
        'result.html',{
            "request":request,
            "surface": surface,
            "pieces": pieces,
            "arrondissement": arrondissement,
            "prix_m2":round(prix_m2, 2),
            "prix_total":round(prix_total,2)
        }
    )