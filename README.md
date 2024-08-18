# final_project

# Image Classification of Coins with Jetson Nano

This project demonstrates the power of NVIDIA's Jetson Nano by using a ResNet-18 model to classify images. It’s a simple yet effective example of how deep learning can be leveraged on edge devices for image recognition tasks. Whether you're new to AI or have some experience, this project showcases the potential of AI in a compact, easy-to-understand way. 

This project classifies among different coins: chinese, european, indian, japanese, mexican, us.

## Dataset

I got this dataset from Kaggle containing around 1,500 images. 

Here is the link to the data: [Count Coins Image Dataset](https://www.kaggle.com/datasets/balabaskar/count-coins-image-dataset)

## The Algorithm

The code utilizes the Jetson Nano’s capabilities to load an image, apply a pre-trained ResNet-18 model, and classify the image based on the model’s learned features. Here's a quick breakdown of how it works:

1. **Image Loading:** The image specified by the user is loaded using Jetson's `jetson_utils.loadImage()` function.
2. **Model Selection:** The code loads a ResNet-18 model using `jetson_inference.imageNet()`. The model is set to look for specific input and output blobs, which are the layers where data is fed into and output from the network.
3. **Classification:** The image is processed by the model, which outputs the class index and confidence level. The class description is then retrieved and printed, showing what the image is recognized as and with what confidence level.

This process makes it easy to classify images with a relatively small amount of code, thanks to the Jetson Nano's optimized libraries and pre-trained models. The accuracy and speed make this setup ideal for various real-time applications, from security systems to wildlife monitoring.

## Running this Project

To run this project on your Jetson Nano, follow these steps:

1. **Install Jetson Inference Library:**
   Make sure the Jetson Inference library is installed on your device. If you haven't already, you can follow the [official guide](https://github.com/dusty-nv/jetson-inference) to get it set up.

2. **Download or Clone the Repository:**
   Clone this repository to your Jetson Nano:
   `git clone <repository_url>`

3. **Prepare Your Image:**
   Have an image file ready that you want to classify. Make sure it's accessible from your Jetson Nano.

4. **Run the Code:**
   Execute the script by specifying the filename of the image:
   `python3 coin_code.py <example_image>.jpg`

5. **View the Results:**
   The terminal will display the image's classification along with the confidence percentage. For example:
   image is recognized as 'european' (class #1) with 43.454221% confidence

### Dependencies
- Jetson Inference Library
- Python 3.6+
- Jetson Nano with JetPack installed

That’s it! With just a few steps, you can run image classification on your Jetson Nano and explore the capabilities of AI at the edge.

View a live demonstration of the functional project [here](https://drive.google.com/file/d/18omo6IGDJmWqJe-iQPRfKHWDtcOYkMlg/view?usp=sharing)
