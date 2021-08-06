# Duke Human Resources Chatbot 
## What is this?
This project is an instance of an IBM Watson Assistant Chatbot. Its knowledge base is the hr.duke.edu website.
The content of this chatbot is located in the Watson_assistant directory, and is in .json format. The goal of this chatbot
is to have a 24/7 online chatbot that can answer user's human resources-related questions in an efficient manner.
## How to build
1. Fork and clone the repository onto your local machine.
2. To create your own instance of this chatbot, create your own Watson Assistant at https://cloud.ibm.com/catalog/services/watson-assistant. 
3. After making a new Assistant, launch the Assistant and create a new dialog skill. Choose to "upload skill," and import the json file located in the Watson_assistant directory.
4. SSH into your virtual machine, and fork/clone this repository.
5. Build the docker containers with the command:

`sudo docker-compose up -d`

## How to Access
Go to the [test website](https://chatbot-test-01.oit.duke.edu/ "Named link title"), and click the icon in the lower right corner to start talking to the chatbot.

## Infrastructure
![Infrastructure Slide](/Users/emilyhughes/Downloads/Slide1.jpeg)
