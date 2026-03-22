# 🤖 AI Chatbot Assistant (Django)

Welcome to the **AI Chatbot Assistant**, a sleek, ultra-premium web application built with Django that allows users to interact with Meta's Llama 3.3 70B AI model using the Together AI API.

This project pairs a robust backend with a stunning, futuristic frontend UI to deliver an immersive chatting experience.

## ✨ Features

- **Brainy AI**: Powered by `meta-llama/Llama-3.3-70B-Instruct-Turbo` via Together AI for blazing fast and intelligent responses.
- **Ultra-Premium UI**:
  - **Futuristic Dark Mode**: A deep, 4-color animated gradient background.
  - **Deep Glassmorphism**: Frosty, semi-transparent chat containers that capture the futuristic vibe.
  - **Micro-Animations**: Smooth sliding bubbles, glowing inputs, and vibrant button hover effects.
  - **Loading States**: Real-time visual feedback (spinners) preventing double submissions.
- **Responsive Design**: Flawlessly adapts to desktop screens and mobile devices.

## 🛠️ Technology Stack

- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **API Integration**: Together AI (REST API via `requests`)
- **Typography**: Google Fonts (Inter)

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/balajiinfo8/AskAI-Django-Assistant.git
   cd AskAI-Django-Assistant
   ```

2. **Create a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   Make sure you have Django and the requests library installed:
   ```bash
   pip install django requests
   ```

4. **Set your API Key:**
   The application uses the Together AI API. Ensure you have your API key set in your `settings.py` (or through environment variables if configured):
   ```python
   TECHBRAIN_API_KEY = "your_together_api_key_here"
   ```

5. **Run Database Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```
   The app will be available at `http://127.0.0.1:8000/`.

## 🎨 UI/UX Highlights
- **Typography:** Uses the modern **Inter** font for superior readability.
- **Animations:** Custom CSS `keyframes` to provide organic movement to gradients and pop-in effects for AI messages.
- **Form Handling:** Submits data cleanly back to the Django view, retaining the conversation flow state via Python logic.

## 🤝 Contributing
Feel free to fork this project, submit pull requests, or send suggestions to make this chatbot even smarter and more beautiful!
