"""
File: main.py
Author: Yassine El Yacoubi
Description: Main application script to integrate image description and speech recognition into a multi-modal AI pipeline.
Dependencies: Hugging Face Transformers, Local Modules (image_description, speech_recognition)

Steps:
    - Calls generate_image_description() to process an image.
    - Calls speech_to_text() to capture voice input.
    - Combines inputs and uses GPT-3.5 to generate a response.

"""

from transformers import pipeline
from image_description import generate_image_description
from speech_recognition import speech_to_text

# Load the text generation pipeline
text_generator = pipeline("text-generation", model="gpt-3.5-turbo")

def main():
    """
    Main function to integrate multi-modal inputs and generate AI responses.
    """
    # Get the image description
    image_path = "example_image.jpg"  # Replace with the path to your image
    image_description = generate_image_description(image_path)

    # Get the spoken input
    spoken_input = speech_to_text()

    # Combine inputs and generate output
    prompt = f"The image shows: {image_description}. The user said: {spoken_input}. Provide a response:"
    response = text_generator(prompt, max_length=100, num_return_sequences=1)

    print("AI Response:", response[0]['generated_text'])

if __name__ == "__main__":
    main()
