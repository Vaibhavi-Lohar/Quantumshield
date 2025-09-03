# 🔐 QuantumShield Backend

Backend service for **QuantumShield**, a project developed during the Prarambha – DKTE Hackathon 2025.  
This backend provides APIs for detecting AI-generated digital content (images, audio, video) and integrates with Firebase and external APIs.

---

## ⚙️ Setup Instructions

### 1️⃣ Navigate to the project folder
Open your terminal or PowerShell and move into the project directory:
```bash
cd QuantumShield
```
### 2️⃣ Create and activate virtual environment
python -m venv venv

Activate it:

Windows (PowerShell)-

.\venv\Scripts\activate

Linux/Mac-

source venv/bin/activate

### 3️⃣ Install dependencies

Make sure you have a requirements.txt file with the following content:

fastapi
uvicorn
opencv-python
librosa
numpy
pydantic
python-multipart
requests
transformers
firebase-admin


Install them:

pip install -r requirements.txt

### 4️⃣ Run the backend server
uvicorn app:app --reload --port 8000


Server runs at 👉 http://127.0.0.1:8000

### 5️⃣ Expose Backend with Public URL (Ngrok)

By default, the backend runs only on `http://127.0.0.1:8000` (local machine).  
To make it accessible from mobile apps or external systems, we used **Ngrok**.

#### Install Ngrok
Download Ngrok from the official website:  
👉 https://ngrok.com/download

Extract/Install it, then log in with your Ngrok auth token:
```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN
```
Start Ngrok

Run this in a new terminal (keep your backend running in another terminal):

ngrok http 8000


This will generate a public forwarding URL like:

https://abcd-1234-56-78.ngrok-free.app


Use this URL in your Android app or frontend instead of http://127.0.0.1:8000.

