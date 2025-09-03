📱 QuantumShield – Android App

QuantumShield is an Android application built during the Prarambh Hackathon 2025 (DKTE College, DSSA Committee).
The app acts as a digital shield that protects users from fake media, scam messages, and fraud threats.

🚀 Features

🔑 Firebase Authentication – Secure login & registration system.

📸 Upload & Detect – Users can upload images, videos, or audio to check if they are fake/AI-generated.

💬 Message Checker – Paste SMS/links to detect scams or phishing attempts.

🌍 Google Maps Integration – Visualize suspicious phone numbers and activities on a map.

🎨 Modern UI – Splash screen, custom buttons, animations, and background themes.

🛠️ Tech Stack

Language: Java ☕

IDE: Android Studio 🖥️

Backend API: Connected to FastAPI (Python) using Retrofit + OkHttp

Database & Authentication: Firebase 🔥

UI/UX: XML layouts + custom styles

⚡ How It Works

User registers/login via Firebase.

From the main screen, user can:

Upload image/video/audio → sent to backend for analysis.

Paste a message/link → checked for fraud.

View suspicious activity on Google Maps.

The app displays results with:

Label (Real / Suspicious)

Confidence score

Explanations

📂 Project Structure
QuantumShield-Android/
 ├── app/
 │   ├── src/                  # Java + XML source code
 │   │   ├── activities/       # Login, Register, Main, Splash
 │   │   ├── api/              # Retrofit API & models
 │   │   └── utils/            # Helpers
 │   ├── build.gradle.kts
 │   ├── google-services.json  # Firebase config
 │   └── proguard-rules.pro
 ├── gradle/                   # Gradle wrapper
 ├── gradlew / gradlew.bat
 ├── build.gradle.kts          # Project-level Gradle
 ├── settings.gradle.kts
 └── README.md

🏆 Hackathon Info

Event: Prarambh Hackathon 2025

Organizers: DKTE College, DSSA Committee

Collaboration: Google AI & IIT Bombay

Build Time: 6 hours 🚀

👨‍💻 Developer (Android App)

Satyam – Android app development (Firebase, API integration, UI/UX Design, Retrofit networking).

(Other teammates handled backend & AI logic in a separate repo)


✨ This Android app is the frontend engine of QuantumShield, empowering users to fight cyber threats with AI.

#Android #Java #Firebase #Retrofit #QuantumShield #Hackathon #CyberSecurity