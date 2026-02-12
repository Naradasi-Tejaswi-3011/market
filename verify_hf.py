import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv('HUGGING_FACE_API_KEY')
HF_IMAGE_MODEL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

def test_hf_generation():
    if not HF_API_KEY:
        print("FAIL: HUGGING_FACE_API_KEY is missing in .env")
        return

    print(f"Testing HF API with model: {HF_IMAGE_MODEL}")
    prompt = "Modern professional SaaS marketing poster background, abstract tech gradient, minimal clean layout, no text"
    
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt, "options": {"wait_for_model": True}}
    
    try:
        response = requests.post(HF_IMAGE_MODEL, headers=headers, json=payload)
        
        if response.status_code == 200:
            print(f"SUCCESS: Image generated successfully. Buffer size: {len(response.content)} bytes")
            with open("test_bg.jpg", "wb") as f:
                f.write(response.content)
            print("Saved test image to test_bg.jpg")
        else:
            print(f"FAIL: API returned status {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    test_hf_generation()
