from fastapi import FastAPI
from app.scanner import scan_apps
from app.validator import validate_apps

app = FastAPI()

@app.get("/scan")
def scan():
    return {"applications": scan_apps()}

@app.get("/validate")
def validate():
    apps = scan_apps()
    return {"validation": validate_apps(apps)}

@app.get("/health")
def health():
    return {"status": "ok"}