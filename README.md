# 🎬 Muvio – AI That Knows Your Next Movie

**A Hybrid AI Movie Recommendation System that combines Large Language Models (LLMs) with a custom recommendation pipeline.**

---

## 📖 Overview

**Muvio** is a conversational AI movie recommendation system developed in **Python** as part of the **LPU Engage – Advanced Python Project**.

Instead of allowing an AI model to directly recommend movies, Muvio follows a **Hybrid AI Architecture**. Google Gemini is used only to understand user intent and extract structured preferences such as genre, language, actors, director, producer,  duration or release year.

These preferences are then passed to Muvio's own recommendation pipeline, where custom filtering, and response generation are performed before presenting the final result to the user.

This approach provides greater control, consistency, and flexibility compared to relying entirely on AI-generated responses.

---

# 🏗 Hybrid AI Architecture

Unlike traditional AI chatbots, Muvio separates **AI understanding** from **application logic**.

### Workflow

```text
User Input (Voice/Text)
          │
          ▼
Speech Processing
          │
          ▼
Intent & Preference Extraction
(Google Gemini)
          │
          ▼
Custom Recommendation Pipeline
(Filter • Response Logic)
          │
          ▼
Formatted Recommendation
          │
          ▼
Voice + Text Response
```

---

## 💡 Why This Architecture?

Using Gemini only for language understanding allows Muvio to keep recommendation logic under developer control.

Benefits include:

- Better recommendation consistency
- Easier customization
- More accurate response
- Scalable architecture
- Clear separation between AI and business logic
- Modular and maintainable codebase

This design pattern is commonly used in modern software systems.

Examples:

- **Netflix** uses AI to understand user interests, while recommendation ranking is handled by dedicated backend algorithms.
- **Spotify** uses AI to understand listening behavior, but playlist generation and ranking are managed by its recommendation system.
- **Amazon** uses AI for search understanding, while product ranking and recommendations are controlled by separate application logic.

---

# ✨ Features

- 🎤 Voice interaction
- ⌨️ Text interaction
- 🤖 Intelligent preference extraction using Google Gemini
- 🎬 Custom recommendation pipeline
- ⭐ Movie details (Rating, Genre, Year, Languages, Actors, Directors, Producers, Title, Lenght, Industry)
- 💬 Natural conversational responses
- 🔊 AI voice output
- 📦 Modular Python architecture

---

# 🛠 Technologies Used

- Python
- Google Gemini API
- SpeechRecognition
- Edge-TTS
- PyAudio
- Pygame
- Python Dotenv

---

# ⚙ Technical Highlights

- Hybrid AI Recommendation System
- Intent Recognition
- Structured Parameter Extraction
- Custom Recommendation Pipeline
- Context-Aware Responses
- Speech-to-Text (STT)
- Text-to-Speech (TTS)
- Modular Software Design

---

# 📁 Project Structure

```text
Muvio/
│
├── muvio.py
├── config.py
├── prompts.py
├── movie_search_algorithm.py
├── speaking.py
├── listning.py
├── talking_type.py
├── requirements.txt
└── .env
```

---

# 🚀 Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the project:

```bash
python muvio.py
```

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- AI-assisted Software Development
- Large Language Model (LLM) Integration
- API Integration
- Recommendation System Design
- Voice Processing
- Modular Programming
- Python Application Development

---

# 👨‍💻 Developer

**Mohd Zaid**

B.Tech Computer Science & Engineering

Lovely Professional University

LPU Engage – Advanced Python Project