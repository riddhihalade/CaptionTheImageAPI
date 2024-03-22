from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from PIL import Image
import io
from model import image_to_text

# Read the description from a file
with open("description.md", "r") as file:
    api_description = file.read()

app = FastAPI(
    title="Image Caption Generator API",
    description=api_description,
    version="1.0.0",
    contact={
        "name": "Riddhi Halade",
        "email": "haladeriddhi@gmail.com",
    }
)

class ImageCaption(BaseModel):
    caption: str

@app.post("/predict/")
def predict(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        image = Image.open(io.BytesIO(contents))
        result = image_to_text([image])
        return ImageCaption(caption=result[0])
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid image file")

@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse(url="/docs")
    
