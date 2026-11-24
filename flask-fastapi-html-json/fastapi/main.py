from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# Import the items router
from api.items import router as items_router

# Create a FastAPI app instance
app = FastAPI()

# Create a Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Sample user data
users = {
    "username": "Jaswanth",
    "email": "ssjaswanth696@gmail.com"
}

# Register APIRouter
app.include_router(items_router)

# Profile HTML route
@app.get("/profile")
async def profile(request: Request):
    # Render the profile.html template with user data
    return templates.TemplateResponse(
        request=request,
        name="profile.html",
        context={
            "user": users
        }
    )
