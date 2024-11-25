# Multi-sensory GenAI 

## Author
**Yassine El Yacoubi**

## Overview
This project showcases a multi-sensory AI that integrates image description and voice recognition to generate meaningful responses using a Large Language Model (LLM). The application processes:
1. **Images**: Describes the content of an image using BLIP.
2. **Speech**: Captures and transcribes spoken input via Google Speech Recognition.
3. **Text Generation**: Combines the image description and transcribed speech to generate a contextual response using GPT-3.5.

The project highlights how multi-modal AI systems can enhance interactivity and provide intelligent, context-aware responses.
Learn more at Medum blog article[Expanding Beyond Text: A Practical Guide to Building Multi-Modal LLM Solutions](https://medium.com/@yassine.elyacoub/expanding-beyond-text-a-practical-guide-to-building-multi-modal-llm-solutions-426a6f0f94a8)
Follow my blogs at [Medium LLM-related blogs](https://bit.ly/yassine-blogs]

---

## Features
- **Image Processing**: Automatically analyzes and generates descriptions for uploaded images.
- **Voice Recognition**: Captures user speech and converts it to text in real-time.
- **Text Generation**: Creates meaningful responses by combining multi-modal inputs.

---

## File Structure

├── image_description.py # Function for generating image descriptions using BLIP. 
├── speech_recognition.py # Function for capturing and transcribing voice input. 
├── main.py # Main script that integrates all functionalities. 
└── README.md # Documentation for the project.

---

## Prerequisites
- Python 3.7 or higher
- Install dependencies:
  ```bash
  pip install transformers pillow speechrecognition flask

How to Run

    Clone the repository:

git clone https://github.com/your-repo/multi-modal-ai.git
cd multi-modal-ai

Start the Flask app:

    python app.py

    Open your browser and go to http://127.0.0.1:5000.

Usage

    On the main page, upload an image.
    Provide voice input when prompted.
    View the AI-generated response combining the image description and your spoken input.

Example Output

Image Description: "A sunset over a mountain range."
Spoken Input: "Tell me something interesting about this scene."
AI Response: "This serene scene represents the beauty of nature, with the sun setting over rugged mountains."
References

    Expanding Beyond Text: A Practical Guide to Building Multi-Modal LLM Solutions
    Hugging Face Transformers Documentation
    BLIP Model on Hugging Face
    Google Speech Recognition Documentation

License

This project is licensed under the MIT License.


---

### **How It All Fits Together**
- The `app.py` file creates a simple Flask web server.
- Templates in the `templates/` folder provide the frontend for uploading images and displaying results.
- `image_description.py` and `speech_recognition.py` handle the core multi-modal processing logic.
- The `README.md` explains the setup and usage of the project.
