from flask import Flask, request, jsonify
import requests
from retell import Retell

app = Flask(__name__)

# VAPI API URL and token
VAPI_URL = "https://api.vapi.ai/assistant"  # Corrected endpoint for creating assistant
VAPI_TOKEN = "ac861e19-d6f2-4fae-b9fe-85cd72f13a92"  # Replace with your actual VAPI API token

# Retell API key
RETELL_API_KEY = "agent_a6238be26f48bafe1c9e7aea12"  # Replace with your Retell API key

@app.route('/create_agent', methods=['POST'])
def create_agent():
    provider = request.json.get('provider')

    if provider == 'vapi':
        return create_vapi_agent(request.json)
    elif provider == 'retell':
        return create_retell_agent(request.json)
    else:
        return jsonify({"error": "Invalid provider specified"}), 400

def create_vapi_agent(data):
    headers = {
        "Authorization": f"Bearer {VAPI_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "firstMessage": data.get("firstMessage", "Hello!"),
        "name": data.get("name", "My Assistant"),
        "voice": {
            "provider": "playht",
            "voiceId": data.get("voice", "jennifer")
        },
        "model": {
            "provider": "openai",
            "model": data.get("model", "gpt-3.5-turbo")
        },
        "artifactPlan": {
            "recordingEnabled": data.get("recordingEnabled", True)
        },
        "firstMessageInterruptionsEnabled": data.get("interruptionsEnabled", False)
    }

    # VAPI assistant creation request
    response = requests.post(VAPI_URL, headers=headers, json=payload)

    if response.status_code == 201:
        return jsonify({"assistant_id": response.json()["id"]}), 201
    else:
        return jsonify({"error": response.json().get("message", "Failed to create assistant")}), response.status_code

def create_retell_agent(data):
    client = Retell(api_key=RETELL_API_KEY)
    try:
        agent_response = client.agent.create(
            response_engine={
                "llm_id": data.get("llm_id", "llm_default"),
                "type": "retell-llm"
            },
            voice_id=data.get("voice_id", "11labs-Adrian")
        )
        return jsonify({"agent_id": agent_response.agent_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
