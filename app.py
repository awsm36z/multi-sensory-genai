"""
File: app.py
Author: Yassine El Yacoubi
Description: Flask web application to integrate image description and speech recognition with LLM response generation.
Dependencies: Flask, Transformers, Local Modules (image_description, speech_recognition)

Routes:
    - /: Renders the main form.
    - /process: Processes the uploaded image and voice input, and displays the AI-generated response.
"""

from flask import Flask, request, render_template
from transformers import pipeline
from image_description import generate_image_description
from speech_recognition import speech_to_text

app = Flask(__name__)

# Load the text generation pipeline
text_generator = pipeline("text-generation", model="gpt-3.5-turbo")

@app.route("/")
def index():
    """
    Renders the main form for image upload and voice input.
    """
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    """
    Processes the uploaded image and voice input, and generates an AI response.
    """
    # Handle image upload
    uploaded_image = request.files.get("image")
    if not uploaded_image:
        return "No image uploaded!", 400

    image_path = "uploaded_image.jpg"
    uploaded_image.save(image_path)

    # Generate image description
    image_description = generate_image_description(image_path)

    # Capture voice input
    spoken_input = speech_to_text()

    # Generate AI response
    prompt = f"The image shows: {image_description}. The user said: {spoken_input}. Provide a response:"
    response = text_generator(prompt, max_length=100, num_return_sequences=1)

    return render_template(
        "result.html",
        image_description=image_description,
        spoken_input=spoken_input,
        ai_response=response[0]["generated_text"]
    )

if __name__ == "__main__":
    app.run(debug=True)
