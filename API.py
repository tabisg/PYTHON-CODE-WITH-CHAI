from fastapi import FastAPI, UploadFile, File # FastAPI core + file upload tools
from typing import List  # Helps when we want multiple files
import uvicorn    # To run the server

app = FastAPI() # Create the FastAPI app

@app.get('/')   # GET = to "fetch" something
def home():
    return {'data': 'welcome to homepage'}

@app.get('/contact')
def contact():
    return {'data': 'welcome to contact page'}

@app.post('/upload')  # POST = to "send" or "upload" data
async def handleImage(files: List[UploadFile] = File(...)):
    filenames = [file.filename for file in files]  # get all uploaded file names
    return {'status': 'got the files', 'filenames': filenames}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

"""GET = "Just see" (read something).

POST = "Send something" (upload / insert).

UploadFile + File(...) = "Upload required files."

uvicorn.run() = "Start the engine to run the app."""