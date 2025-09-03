# detection.py
import cv2
import numpy as np
import librosa
from transformers import pipeline
import os

# ---------------- CONFIG ----------------
HF_TOKEN = "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"  # Your Hugging Face token
IMAGE_MODEL = "Ateeqq/ai-vs-human-image-detector"

# Initialize the image detection pipeline
image_detector = pipeline(
    "image-classification",
    model=IMAGE_MODEL,
    token=HF_TOKEN
)

# ---------------- IMAGE DETECTION ----------------
def analyze_image(image_path):
    try:
        preds = image_detector(image_path)
        top = preds[0]
        return {
            "label": top["label"],  # expected "AI-generated" or "real"
            "confidence": float(top["score"]),
            "explanations": [f"Predicted as {top['label']} with {top['score']:.2f} confidence."]
        }
    except Exception as e:
        return {"label": "error", "confidence": 0.0, "explanations": [str(e)]}

# ---------------- AUDIO DETECTION (Deepfake Detection HF Model) ----------------
audio_detector = pipeline(
    "audio-classification",
    model="Heem2/Deepfake-audio-detection",
    use_auth_token="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"  # Replace with your Hugging Face token
)

def analyze_audio(audio_path):
    try:
        results = audio_detector(audio_path)
        label = results[0]['label']
        confidence = float(results[0]['score'])
        return {"label": label, "confidence": confidence, "explanations": [f"Audio classified as {label} with confidence {confidence:.2f}"]}
    except Exception as e:
        return {"label": "error", "confidence": 0.0, "explanations": [str(e)]}
    
    # ---------------- VIDEO DETECTION ----------------

# HF image model
image_detector = pipeline(
    "image-classification",
    model="Ateeqq/ai-vs-human-image-detector",
    token="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"
)

def analyze_video(video_path):
    explanations = []
    try:
        cap = cv2.VideoCapture(video_path)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        step = max(1, frame_count // 20)  # sample up to 20 frames

        ai_score_sum = 0.0
        hum_score_sum = 0.0
        high_conf_threshold = 0.95  # only consider strong predictions
        total_used_frames = 0

        for i in range(0, frame_count, step):
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            ret, frame = cap.read()
            if not ret:
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if np.std(gray) < 10:
                explanations.append(f"Frame {i}: Skipped due to low contrast.")
                continue

            frame_path = f"temp_frame_{i}.jpg"
            cv2.imwrite(frame_path, frame)
            result = image_detector(frame_path)[0]
            label = result['label'].lower()
            score = result['score']
            os.remove(frame_path)

            explanations.append(f"Frame {i}: {label} ({score:.2f})")
            total_used_frames += 1

            # Count only high confidence frames
            if score >= high_conf_threshold:
                if "ai" in label:
                    ai_score_sum += score
                elif "hum" in label:
                    hum_score_sum += score

        cap.release()

        if total_used_frames == 0:
            return {
                "label": "error",
                "confidence": 0.0,
                "explanations": explanations + ["No usable frames found."]
            }

        total_score = ai_score_sum + hum_score_sum
        if total_score == 0:
            final_label = "real"
            confidence = 0.0
        else:
            ai_ratio = ai_score_sum / total_score
            final_label = "AI-generated" if ai_ratio >= 0.7 else "real"
            confidence = round(max(ai_ratio, 1 - ai_ratio), 2)

        explanations.append(f"Final decision: {final_label} ({confidence:.2f} confidence based on {total_used_frames} frames)")

        return {
            "label": final_label,
            "confidence": confidence,
            "explanations": explanations
        }

    except Exception as e:
        return {
            "label": "error",
            "confidence": 0.0,
            "explanations": [str(e)]
        }