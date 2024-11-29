import torch
import json
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM

# Configuration
model_id = "meta-llama/Llama-3.2-1B"

# Chargement de la configuration et du token API depuis config.json
try:
    config_data = json.load(open('config.json'))
    my_secret_key = config_data['HF_TOKEN']
except Exception as e:
    raise ValueError("Impossible de charger le fichier config.json ou de lire le token HF.") from e

# Chargement du tokenizer et du modèle
try:
    tokenizer = AutoTokenizer.from_pretrained(model_id, token=my_secret_key)
    tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="auto",  # Déplacement automatique sur le GPU si disponible
        token=my_secret_key
    )
except Exception as e:
    raise ValueError("Erreur lors du chargement du modèle ou du tokenizer.") from e

# Initialisation de FastAPI
app = FastAPI()

# Configurer les templates et les fichiers statiques
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Modèle pour les requêtes API (backend)
class Query(BaseModel):
    input_text: str

# Route pour le front-end
@app.get("/", response_class=HTMLResponse)
async def serve_frontend(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": None})

# Route pour soumettre un texte via le front-end
@app.post("/", response_class=HTMLResponse)
async def submit_text(request: Request, input_text: str = Form(...)):
    try:
        # Préparer l'entrée
        inputs = tokenizer(input_text, return_tensors="pt", padding=True).to("cpu")
        # Génération de texte
        outputs = model.generate(
            inputs["input_ids"],
            max_length=150,
            temperature=0.4,
            top_k=50,
            top_p=0.95,
            num_return_sequences=1
        )
        # Décoder la réponse
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return templates.TemplateResponse(
            "index.html", {"request": request, "response": response, "input_text": input_text}
        )
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "response": f"Erreur : {str(e)}", "input_text": input_text}
        )

# Exemple pour vérifier l'accès au modèle et au tokenizer
@app.get("/check")
async def check_model():
    return {
        "model_id": model_id,
        "tokenizer_status": "Loaded",
        "model_status": "Loaded",
    }
