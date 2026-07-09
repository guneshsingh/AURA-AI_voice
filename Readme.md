<div align="center">

# 🤖 AURA — AI Voice Assistant

**A Python-based, wake-word-activated voice assistant powered by Llama 3.3 70B**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/LLM-Groq%20Llama%203.3%2070B-F55036?style=for-the-badge)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#license)
[![Status](https://img.shields.io/badge/Status-Active%20Development-orange?style=for-the-badge)]()

[Features](#-features) • [Tech Stack](#-tech-stack) • [Installation](#-installation) • [Usage](#-usage) • [Roadmap](#-roadmap)

</div>

---

## 📖 About

**AURA** is a voice-controlled desktop assistant built from scratch in Python. It listens for a wake word, understands natural-language commands, and responds with speech — combining classic speech-recognition/TTS pipelines with a modern LLM backend for open-ended conversation.

Say **"Hello"** or **"Aura"** to activate it, then talk naturally — no rigid command syntax required.

## ✨ Features

- 🎙️ **Wake-word activation** — listens passively and wakes on "hello" / "Aura", with an idle timeout so it doesn't stay hot forever
- 🔁 **Continuous command mode** — once activated, keeps listening for follow-up commands without needing to repeat the wake word every time
- 🧠 **LLM-powered conversation** — general queries are handled by **Llama 3.3 70B** via Groq's OpenAI-compatible API for fast, natural responses
- 🌐 **Flexible web & music commands** — natural-language, substring-based matching against a `websites` dictionary, so phrasing doesn't have to be exact (e.g. "open YouTube" and "can you open youtube for me" both work)
- 🎵 **Music library integration** — plays songs from a curated `musiclibrary.py` mapping via the browser
- 📰 **Live news headlines** — fetches current headlines through the NewsAPI
- 🔊 **Text-to-speech feedback** — responses are spoken back using `pyttsx3` (SAPI5 engine on Windows), reinitialized per call to avoid the engine going silent after first use

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Speech recognition | `speech_recognition` |
| Text-to-speech | `pyttsx3` (sapi5) |
| Conversational AI | Llama 3.3 70B via Groq (OpenAI-compatible SDK) |
| News | NewsAPI |
| Web/media control | `webbrowser` |
| Language | Python 100% |

## 📂 Project Structure

```
AURA-AI_voice/
├── main.py             # Entry point — wake word, listening loop, command routing
├── musiclibrary.py     # Song name → URL mapping used by music commands
├── test.py             # Scratch/testing script
├── requirements.txt    # Python dependencies
├── .env.example        # Template for required API keys
├── .gitignore
├── LICENSE             # MIT License
└── README.md
```

## 🚀 Installation

**Prerequisites:** Python 3.10+, a working microphone, and API keys for Groq and NewsAPI.

```bash
# 1. Clone the repo
git clone https://github.com/guneshsingh/AURA-AI_voice.git
cd AURA-AI_voice

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt
```

> 💡 On Windows, `pyaudio` sometimes needs a prebuilt wheel — if it fails to install, run `pipwin install pyaudio` instead.

### Configure API keys

Copy the example env file and fill in your own keys:

```bash
cp .env.example .env    # macOS/Linux
copy .env.example .env  # Windows
```

Then open `.env` and add your keys:

```env
GROQ_API_KEY=your_groq_api_key_here
NEWSAPI_KEY=your_newsapi_key_here
```

`.env` is listed in `.gitignore` and should **never** be committed — only `.env.example` (with placeholder values) is tracked in the repo. Load the real keys in `main.py` with `python-dotenv` (`load_dotenv()`) rather than hardcoding them.

## ▶️ Usage

```bash
python main.py
```

1. AURA starts listening passively for the wake word.
2. Say **"Hello"** to activate.
3. Speak your command — open a website, play a song, ask for news, or just chat.
4. AURA stays in an active listening loop until the idle timeout kicks in, so you can issue multiple commands without repeating the wake word.

**Example commands:**
- "Open YouTube"
- "Play [song name]"
- "What's the news today?"
- "What's the capital of France?" *(routed to the LLM for general conversation)*

## 🗺️ Roadmap

- [ ] Cross-platform TTS support (currently SAPI5/Windows-oriented)
- [ ] Custom wake-word training instead of keyword matching
- [ ] Plugin-style command architecture for easier extension
- [ ] Add unit tests around command matching

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/guneshsingh/AURA-AI_voice/issues) or open a pull request.

## 📄 License

This project is licensed under the [MIT License](LICENSE) — free to use, modify, and distribute.

## 👤 Author

**Gunesh Singh**
B.Tech CSE student • SDE aspirant • DSA enthusiast

[![GitHub](https://img.shields.io/badge/GitHub-guneshsingh-181717?style=flat-square&logo=github)](https://github.com/guneshsingh)
[![LeetCode](https://img.shields.io/badge/LeetCode-keep__up__gun-FFA116?style=flat-square&logo=leetcode&logoColor=white)](https://leetcode.com/keep_up_gun)

---

<div align="center">
<i>⭐ If you find AURA interesting, consider starring the repo!</i>
</div>
