# AI Agent API

This Flask application provides a unified API to create AI agents using either the Vapi or Retell platforms.


### POST /create_agent

Creates an AI agent on the specified platform.

#### Request Body

```json
{
  "provider": "vapi" | "retell",
  "firstMessage": "Hello!",
  "model": "gpt-3.5-turbo",
  "voice": "jennifer-playht",
  "recordingEnabled": true,
  "interruptionsEnabled": false,
  "llm_id": "llm_default",
  "voice_id": "11labs-Adrian"
}
