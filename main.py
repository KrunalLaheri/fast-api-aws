from fastapi import FastAPI, Request, HTTPException, status, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi import FastAPI, Form, Response
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException, Request
# Create an instance of FastAPI
app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Render the HTML page using the template
    return templates.TemplateResponse("login.html", {"request": request})

# To run the app, use the command: uvicorn main:app --reload
class User(BaseModel):
    email: str
    password: str

# A sample user database
# In a real-world application, you should use a database or external service to manage users and passwords
user_db = {
    "krunal@gmail.com": "krunal"
}


@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, user: User):
    # Check if the provided email and password match a user in the database
    email = user.email
    password = user.password
    
    if email in user_db and user_db[email] == password:
        # Return a successful response
        return templates.TemplateResponse("home.html", {"request": request})

    else:
        # Return an error response for invalid credentials
        raise HTTPException(status_code=401, detail="Invalid email or password")

# Run the app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)