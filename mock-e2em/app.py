from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/traces/{app_name}")
def get_trace(app_name: str):
    if app_name == "app1":
        return {"trace": "exists"}
    raise HTTPException(status_code=404, detail="not found")