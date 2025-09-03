from fastapi import FastAPI, UploadFile, File, Form
import os
import shutil

# Import your detection functions
from ai.detection import analyze_image, analyze_video, analyze_audio

# Create FastAPI app
app = FastAPI()

# Folder to save uploaded files temporarily
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# API endpoint: /analyze
@app.post("/analyze")
async def analyze(
    mediaType: str = Form(...),   # image / video / audio
    file: UploadFile = File(...)  # uploaded file
):
    # Define temporary file path
    temp_file_path = os.path.join(UPLOAD_DIR, f"temp_{file.filename}")

    # Save the uploaded file temporarily
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # Call the correct detection function
        if mediaType == "image":
            result = analyze_image(temp_file_path)
        elif mediaType == "video":
            result = analyze_video(temp_file_path)
        elif mediaType == "audio":
            result = analyze_audio(temp_file_path)
        else:
            return {"error": "Invalid mediaType. Use 'image', 'video', or 'audio'."}

        # Add human-friendly message
        result["message"] = (
            f"This file is likely {result['label']} "
            f"with confidence {result['confidence']:.2f}"
        )

        return result

    except Exception as e:
        return {
            "label": "error",
            "confidence": 0.0,
            "explanations": [f"Internal server error: {str(e)}"]
        }
