from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI CI/CD Pipeline Active. This is the GET endpoint."}

# SEARCH API
@app.get("/search")
def search():
    return HTMLResponse("<html><body>INSIDE SEARCH API..</body></html>")

# VIEW API
@app.get("/view")
def view():
    return HTMLResponse("<html><body>INSIDE VIEW API..</body></html>")

# LOGIN API
@app.post("/login")
def login():
    return HTMLResponse("<html><body>INSIDE LOGIN API..</body></html>")

# UPDATE API
@app.put("/updateprofile")
def update_profile():
    return HTMLResponse("<html><body>INSIDE UPDATE PROFILE API..</body></html>")

# DELETE API
@app.delete("/del")
def delete():
    return HTMLResponse("<html><body>INSIDE DELETE API..</body></html>")