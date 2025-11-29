# chatbot/together_client.py

# 1. Import All Modules requests , os , django.settings
import requests
import os
from django.conf import settings

# 2. Class 
class TogetherAIClient:
    # 3 . class with all information onces 
    def __init__(self):
        # 4. all information helps to communicate with API 
        self.api_url = "https://api.together.xyz/v1/chat/completions"
        self.api_key = settings.TECHBRAIN_API_KEY
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    # 5 . Display the Response From AI server  
    def get_response(self, user_message):

        # 6. way to get the response from the AI server 
        
        data = {
            "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            
            # 7. How many tokes to generate in max 
            "max_tokens": 2000,
            "temperature": 0.7
        }

        # 8. Check response from TogetherAI 
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=data,
                timeout=10
            )
            response.raise_for_status()
            json_repo = response.json()

            # ✅ FIXED: TogetherAI does NOT return "output"
            # Correct JSON path:
            # json_repo["choices"][0]["message"]["content"]
            return json_repo.get("choices", [{}])[0].get("message", {}).get("content", "no content")

        except requests.exceptions.RequestException as e:
            return f"Request Error : {str(e)}"

        except Exception as e:
            return f"Exception Error : {str(e)}\nRaw: {response.text}"
