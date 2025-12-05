#!/usr/bin/env python
# coding: utf-8

# In[5]:


from fastapi import FastAPI, UploadFile, File
import whisper
import shutil

app = FastAPI()

model = whisper.load_model("small")

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    with open("temp.wav", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = model.transcribe("temp.wav", language="ar")
    return {"text": result["text"]}

