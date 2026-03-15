RICO UI Captioner
Vision-Language Model for Automatic Mobile UI Screen Captioning
Overview

RICO UI Captioner is a vision-language model designed to automatically generate natural language descriptions of mobile application user interface (UI) screenshots.

The system uses a fine-tuned version of BLIP to understand UI layouts and produce captions describing the content of the screen.

The model is trained on UI screenshots from the RICO Dataset, enabling it to learn patterns such as:

Navigation bars

Buttons

Icons

Form fields

Lists

UI layouts

This project demonstrates how vision-language models can be adapted for UI understanding tasks.

Demo Example

Example UI screenshot:

[ Mobile App Screen ]
--------------------------------
| Profile                       |
| Name: John Doe                |
| Email: john@email.com         |
| [Edit Profile]                |
| [Logout]                      |
--------------------------------

Generated caption:

A mobile application screen showing user profile details with edit and logout options.
Model

Base model:
BLIP

Fine-tuned model hosted on Hugging Face:

surabhimuralidhar/rico-ui-captioner-final

Hugging Face model page:

https://huggingface.co/surabhimuralidhar/rico-ui-captioner-final
Dataset

Training dataset:

RICO Dataset

Dataset characteristics:

Feature	Value
Screenshots	66,000+
Platforms	Android apps
UI Components	Buttons, icons, lists
Categories	Shopping, messaging, travel, etc

Dataset link:

https://interactionmining.org/rico
Model Architecture

The model uses a vision-language transformer architecture.

            +-------------------+
            |   UI Screenshot   |
            +---------+---------+
                      |
                      v
            +-------------------+
            |   Vision Encoder  |
            |  (BLIP Image CNN) |
            +---------+---------+
                      |
                      v
            +-------------------+
            |  Cross Attention  |
            |  Vision ↔ Text    |
            +---------+---------+
                      |
                      v
            +-------------------+
            |   Text Decoder    |
            |  Transformer LM   |
            +---------+---------+
                      |
                      v
            Generated Caption
Training Pipeline

The training process involved several stages.

UI Screenshots
      │
      │
      ▼
Dataset Preparation
(Image, Caption pairs)
      │
      │
      ▼
Pretrained BLIP Model
      │
      │
      ▼
LoRA Fine-Tuning
(Parameter Efficient Training)
      │
      │
      ▼
Fine-Tuned Model
      │
      │
      ▼
Upload to Hugging Face Hub

Fine-tuning method used:

LoRA

Benefits of LoRA:

Reduces training parameters

Lower GPU memory usage

Faster fine-tuning

Project Structure
rico-ui-captioner
│
├── train.ipynb
│
├── inference.py
│
├── requirements.txt
│
└── README.md

File descriptions:

File	Description
train.ipynb	Notebook used to train the model
inference.py	Script to generate captions
requirements.txt	Dependencies
README.md	Documentation
Installation

Clone the repository:

git clone https://github.com/yourusername/rico-ui-captioner.git
cd rico-ui-captioner

Install dependencies:

pip install -r requirements.txt
Requirements

Example requirements file:

torch
torchvision
transformers
datasets
accelerate
peft
pillow
requests
tqdm
numpy
huggingface-hub
sentencepiece
Running Inference

You can generate captions using the provided inference script.

Run:

python inference.py
Inference Code Example

This example downloads the model from Hugging Face and generates a caption.

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests
from io import BytesIO

model = BlipForConditionalGeneration.from_pretrained(
    "surabhimuralidhar/rico-ui-captioner-final"
)

processor = BlipProcessor.from_pretrained(
    "surabhimuralidhar/rico-ui-captioner-final"
)

url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/coco_sample.png"

image = Image.open(BytesIO(requests.get(url).content)).convert("RGB")

inputs = processor(images=image, return_tensors="pt")

output = model.generate(**inputs)

caption = processor.decode(output[0], skip_special_tokens=True)

print("Generated Caption:", caption)

Example output:

Generated Caption:
a mobile application interface with multiple options and icons
Reproducibility

To reproduce the model results:

Download the dataset

Run the training notebook

Fine-tune BLIP using LoRA

Save the trained model

Upload the model to Hugging Face

Training environment:

Component	Value
Framework	PyTorch
Library	Transformers
Training Platform	Google Colab
GPU	NVIDIA T4
Applications

This system can be used in multiple domains.

UI Accessibility
Automatically describe UI screens for visually impaired users.

UI Search
Search UI screenshots using text queries.

Automated UI Documentation
Generate descriptions of application screens.

UI Design Analysis
Study patterns in application design.

Limitations

The model may have limitations including:

Generic captions for complex layouts

Difficulty recognizing small UI elements

Limited understanding of app context

Future Work

Potential improvements include:

Component-level UI captioning

Larger UI datasets

Multilingual captions

Integration with UI detection models

Real-time UI analysis systems

Citation

If you use this work, please cite:

@misc{rico_ui_captioner,
  title={RICO UI Captioner: Vision-Language Model for UI Screen Captioning},
  author={Surabhi Muralidhar},
  year={2026},
  url={https://huggingface.co/surabhimuralidhar/rico-ui-captioner-final}
}
Author

Surabhi Muralidhar

Acknowledgements

This work builds on research from:

Salesforce Research for BLIP

Stanford University for the dataset

Hugging Face for hosting the mode
