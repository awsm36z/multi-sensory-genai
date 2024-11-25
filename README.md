# Multi-sensory GenAI 

## Author
**Yassine El Yacoubi**

## Overview
This project showcases a multi-sensory AI that integrates image description and voice recognition to generate meaningful responses using a Large Language Model (LLM). The application processes:
1. **Images**: Describes the content of an image using BLIP.
2. **Speech**: Captures and transcribes spoken input via Google Speech Recognition.
3. **Text Generation**: Combines the image description and transcribed speech to generate a contextual response using GPT-3.5.

The project highlights how multi-modal AI systems can enhance interactivity and provide intelligent, context-aware responses.

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
Ensure you have Python installed and the following libraries:
- `transformers`
- `Pillow`
- `speechrecognition`

Install the dependencies:
```bash
pip install transformers pillow speechrecognition

How to Run

    Clone or download this repository:

git clone https://github.com/your-repo/multi-modal-ai.git
cd multi-modal-ai

Ensure all the files are in the same directory.

Replace example_image.jpg in main.py with the path to your image file.

Run the main script:

    python main.py

Usage
Step 1: Image Description

    Provide an image file (e.g., example_image.jpg).
    The application generates a description of the image content.

Step 2: Speech Input

    Speak into the microphone when prompted.
    The application transcribes the spoken input to text.

Step 3: Text Generation

    The application combines the image description and the spoken input.
    It generates a contextual response using GPT-3.5.

Example Output

Image Description: "A peaceful lake surrounded by mountains."
Spoken Input: "What makes this scene so special?"
AI Response: "This serene scene captures the tranquility of nature, with the calm lake reflecting the grandeur of the mountains."
Modules
1. image_description.py

Contains the generate_image_description() function to describe the content of an image using the BLIP model.
Dependencies: Hugging Face Transformers, PIL (Pillow).
2. speech_recognition.py

Contains the speech_to_text() function to capture and transcribe spoken input.
Dependencies: SpeechRecognition.
3. main.py

Integrates the image description and speech recognition functions and generates responses using GPT-3.5.
Dependencies: Transformers, Local Modules (image_description.py, speech_recognition.py).
Future Improvements

    Web Interface: Add a user-friendly UI using Streamlit or Flask.
    Noise Filtering: Improve speech recognition accuracy in noisy environments.
    Multi-Image Support: Extend capabilities to process multiple images simultaneously.

References

    Expanding Beyond Text: A Practical Guide to Building Multi-Modal LLM Solutions
    Explore the concepts and practical details of this project in my detailed blog post.
    Hugging Face Transformers Documentation
    BLIP Model on Hugging Face
    Google Speech Recognition Documentation

License

This project is licensed under the MIT License.


---

### Key Features of the Updated README:
- **Detailed Overview**: Explains the project’s purpose and functionality.
- **File Structure**: Clearly lists and explains the files in the project.
- **Usage Instructions**: Provides step-by-step guidance on running the application.
- **Example Output**: Demonstrates what users can expect from the application.
- **References**: Links to your blog post and relevant documentation for further reading.
