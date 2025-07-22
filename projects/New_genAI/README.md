# 🚀 Tech2Idea Generator

An AI-powered tool that helps developers generate unique project ideas based on their technical skills using Google's Gemini AI.

## Features

- 🤖 AI-powered project idea generation
- 🎯 Domain-specific suggestions
- 📊 Difficulty level estimation
- ⏱️ Time estimation
- 🎨 User-friendly Gradio interface

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
   You can get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Usage

1. Run the application:
   ```bash
   python ui_gradio.py
   ```
2. Open your web browser and navigate to the provided local URL (usually http://127.0.0.1:7860)
3. Enter your skills/technologies (comma-separated)
4. Optionally select a domain
5. Click "Generate Ideas" to get unique project suggestions

## Example Input

```
Skills: Python, HTML, Flask, Machine Learning
Domain: Web Development
```

## Example Output

The AI will generate 3 unique project ideas, including:
- Project Name
- Required Tools/Technologies
- Brief Description
- Difficulty Level
- Estimated Time to Complete

## Requirements

- Python 3.7+
- Google Gemini API key
- Internet connection

## License

MIT License 