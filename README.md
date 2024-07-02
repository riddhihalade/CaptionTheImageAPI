# Image Caption Generator API

## Overview
The Image Caption Generator API is a high-performance tool developed to generate descriptive captions for input images using cutting-edge machine learning techniques.

## Features
- **Efficient Caption Generation:** Utilizes Hugging Face Transformers and a VisionEncoderDecoderModel to provide accurate and descriptive captions.
- **FastAPI Integration:** Built with FastAPI for high-throughput and low-latency API endpoints.
- **Dockerized Deployment:** Containerized with Docker for seamless deployment and scalability across different environments.
- **Performance Optimization:** Optimized for speed by loading and initializing the model once for reduced latency.

## Technical Stack
- **Hugging Face Transformers:** Integrates the VisionEncoderDecoderModel for image captioning.
- **FastAPI:** Modern Python web framework for building APIs with asynchronous capabilities.
- **Docker:** Containerization for easy deployment and environment consistency.
- **PyTorch:** Framework used for implementing machine learning models.

## Usage

### Build the Docker image:
docker build -t image-caption-api .


### Run the Docker container:
docker run -p 8000:8000 image-caption-api
