"""
File: app.py
Author: Yassine El Yacoubi
Description: Flask web application to integrate image description and speech recognition with LLM response generation.
Dependencies: Flask, OpenAI, Local Modules (image_description, speech_recognition)
"""

from flask import Flask, request, render_template
from image_description import generate_image_description
from speech_to_text import speech_to_text
import openai
from utils import load_my_api_key

# Set up Flask app
app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = load_my_api_key()

def generate_response(prompt):
    """
    Generates a response using OpenAI's GPT-3.5-turbo model.

    Args:
        prompt (str): The input prompt for the model.

    Returns:
        str: The generated response.
    """
    
    response = openai.chat.completions.create(
    model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


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
    ai_response = generate_response(prompt)

    return render_template(
        "result.html",
        image_description=image_description,
        spoken_input=spoken_input,
        ai_response=ai_response
    )

if __name__ == "__main__":
    app.run(debug=True)
