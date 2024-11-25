"""
File: image_description.py
Author: Yassine El Yacoubi
Description: Contains a function to generate an image description using BLIP.
Dependencies: Hugging Face Transformers, PIL (Pillow)

Function:
    - generate_image_description(image_path): Generates a description of the provided image.

Parameters:
    - image_path (str): Path to the image file.

Returns:
    - str: Generated description of the image.
"""

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load the model and processor once globally for efficiency
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_image_description(image_path):
    """
    Generates a description of the given image using BLIP.

    Args:
        image_path (str): The path to the image.

    Returns:
        str: The generated description of the image.
    """
    # Load the image
    image = Image.open(image_path)

    # Process the image
    inputs = processor(image, return_tensors="pt")

    # Generate the description
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)

    return caption
