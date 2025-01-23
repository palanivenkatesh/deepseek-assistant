# DeepSeek Voice Chatbot

A Python-based chatbot that interacts with the DeepSeek API for intelligent responses and uses text-to-speech (TTS) via Replicate to provide voice output. This project enables natural language conversations with AI-powered voice responses.

## Features

- 🗣️ Real-time conversational AI
- 🔊 Text-to-speech voice responses
- 🤖 DeepSeek's reasoning capabilities
- 💬 Interactive chat interface
- 🌐 Multi-voice support (via Replicate TTS)

## Prerequisites

- Python 3.7+
- [DeepSeek API Key](https://platform.deepseek.com/api_keys)
- [Replicate API Key](https://replicate.com/account/api-tokens)
- FFmpeg (for audio processing)

## Installation

1. **Clone the repository**:
  ```bash
  git clone https://github.com/palanivenkatesh/deepseek-assistant.git
  cd deepseek-voice-chatbot
  ```

2. **Install Dependencies**:
  ```bash
  pip install openai replicate playsound python-dotenv
  ```

3. **Set up environment variables**:
  ```bash
  echo "DEEPSEEK_API_KEY=your_deepseek_key_here" > .env
  echo "REPLICATE_API_KEY=your_replicate_key_here" >> .env
  ```

## Usage
  ```bash
  python app.py
  ```
```
```

## Important Notes
- **API Costs**: This uses paid APIs from both `DeepSeek` and `Replicate`
- **Voice Options**: Available voices include `af_bella`, `en_mei`, `jp_nana`, etc.
- **Internet Connection**: Required for API access
- **Audio Files**: Temporary WAV files are created in the project directory

