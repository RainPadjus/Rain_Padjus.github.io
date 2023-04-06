# Dog Breed Identifier - GitHub.io Page

This repository hosts the Dog Breed Identifier web application, which uses a pre-trained model to classify dog breeds from images. 
The model is trained with FastAI, fine-tuned ResNet18, and hosted on Hugging Face using Gradio. 
You can access the application at   -[DoggoVision on Hugging Face Spaces](https://huggingface.co/spaces/BrennerFjors/DoggoVision).
                                    -[Github.io page](https://rainpadjus.github.io/).
The repository contains the following file:

1. `index.html`: The main HTML file for the web application, which includes the following features:
   - Header with a title.
   - File input for uploading images.
   - A results section that displays the identified breed and the uploaded image.

The web application is designed using simple CSS for styling and JavaScript for handling user interactions and displaying results. The JavaScript code sends an asynchronous request to the Hugging Face-hosted model to classify the uploaded image and returns the predicted dog breed.

To use the Dog Breed Identifier, simply upload an image of a dog and the application will display the predicted breed along with the uploaded image.
