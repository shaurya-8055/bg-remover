from fastapi import FastAPI, File, UploadFile
from rembg import remove
from fastapi.responses import Response

app = FastAPI()

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    img = await file.read()
    output = remove(img)
    return Response(content=output, media_type="image/png")
