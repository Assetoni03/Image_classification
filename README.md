# Image Classification API using FastAPI and Docker
This is a simple API for image classification using a pre-trained ResNet50 model. It allows users to upload an image, which will be processed and classified by the model. Here's a step-by-step guide on how to use this API and how to run it within a Docker container.

API Endpoints
1. Upload an Image
  - Endpoint: /upload/
  - HTTP Method: POST
  - Input: You can upload an image file using the item field in the request.
  - Output: The API will return the label and confidence score of the image classification.

2. Classify an Image
  - Endpoint: /classify/
  - HTTP Method: POST
  - Input: This endpoint expects a tensor representation of the image.
  - Output: The API will return the label and confidence score of the image classification.
  - How to Use the API
3. Clone the repository to your local machine.
  ```
  git clone https://github.com/Assetoni03/Image_classification
  ```
  
4. Run the API using Uvicorn:
  ```
  uvicorn your_api_file_name:app --host 0.0.0.0 --port 8000
  ```
5. You can now access the API at http://localhost:8000.

# Dockerizing the API
To run this API within a Docker container, you can follow these steps:

1. Build a Docker image from the Dockerfile:
  ```
  docker build -t image-classification-api .
  ```
2. Run a Docker container from the image you just built:
  ```
  docker run -p 8000:8000 image-classification-api
  ```
You can now access the API within the Docker container at http://localhost:8000/docs.

That's it! You now have a Dockerized version of the image classification API. You can deploy and scale it as needed for your application.
