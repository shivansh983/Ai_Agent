import requests

url = "http://127.0.0.1:5000/create_agent"

data = {
    "provider": "vapi",
    "firstMessage": "Hey, this is a test assistant.",
    "name": "TestBot",
    "voice": "jennifer",
    "model": "gpt-3.5-turbo",
    "recordingEnabled": True,
    "interruptionsEnabled": False
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
