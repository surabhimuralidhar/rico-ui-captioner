# RICO UI Captioner

### Vision-Language Model for Automatic Mobile UI Screen Captioning

------------------------------------------------------------------------

## Overview

RICO UI Captioner is a vision-language model that automatically
generates natural language descriptions for **mobile UI screenshots**.

The system fine‑tunes the **BLIP (Bootstrapping Language Image
Pre‑training)** vision‑language model to understand UI layouts and
produce captions describing the screen content.

Possible uses:

-   UI accessibility
-   UI search engines
-   Automated UI documentation
-   Mobile design analysis

------------------------------------------------------------------------

## Model

Base model: **BLIP (Bootstrapping Language Image Pre‑training)**

Fine‑tuned model on Hugging Face:

surabhimuralidhar/rico-ui-captioner-final

Model page:

https://huggingface.co/surabhimuralidhar/rico-ui-captioner-final

------------------------------------------------------------------------

## Dataset

Training dataset: **RICO Dataset**

Dataset features:

-   66,000+ Android UI screenshots
-   UI hierarchy metadata
-   Multiple app categories
-   Real application layouts

Dataset link:

https://interactionmining.org/rico

------------------------------------------------------------------------

## Architecture Diagram

The model follows a **Vision‑Language Transformer pipeline**.

               +--------------------+
               |   UI Screenshot    |
               +---------+----------+
                         |
                         v
               +--------------------+
               |   Vision Encoder   |
               |  (BLIP Image CNN)  |
               +---------+----------+
                         |
                         v
               +--------------------+
               |  Cross Attention   |
               | Image ↔ Text       |
               +---------+----------+
                         |
                         v
               +--------------------+
               |   Text Decoder     |
               | Transformer LM     |
               +---------+----------+
                         |
                         v
                 Generated Caption

------------------------------------------------------------------------

## Training Pipeline

    UI Screenshots
          │
          ▼
    Dataset Preparation
    (Image + Caption pairs)
          │
          ▼
    Pretrained BLIP Model
          │
          ▼
    LoRA Fine‑Tuning
    (Parameter Efficient Training)
          │
          ▼
    Fine‑Tuned Model
          │
          ▼
    Upload to Hugging Face Hub

Training environment:

Framework: PyTorch\
Library: Transformers\
Platform: Google Colab\
GPU: NVIDIA T4

------------------------------------------------------------------------

## Project Structure

    rico-ui-captioner/
    │
    ├── neural_nomads_train.ipynb
    ├── inference.py
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## Installation

Clone the repository:

    git clone https://github.com/yourusername/rico-ui-captioner.git
    cd rico-ui-captioner

Install dependencies:

    pip install -r requirements.txt

------------------------------------------------------------------------

## Requirements

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

------------------------------------------------------------------------

## Running Inference

Run:

    python inference.py

The script will:

1.  Download the model from Hugging Face
2.  Load the processor
3.  Process the image
4.  Generate a caption

------------------------------------------------------------------------

## Example Inference Code

``` python
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
```

------------------------------------------------------------------------

## Example Input and Output

Example UI Screenshot:

![Example
UI](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/coco_sample.png)

Generated caption:

"Two cats sleeping on a couch."

------------------------------------------------------------------------

## Approach

The goal of this project is to generate natural language descriptions for mobile UI screenshots using a vision-language model.

The approach consists of the following steps:

1. Dataset Selection

The RICO Dataset was used as the primary dataset. It contains thousands of Android application screenshots along with UI hierarchy information.

2. Model Selection

The project uses the BLIP architecture, which is a vision-language transformer designed for image captioning tasks.

BLIP was chosen because it:

supports multimodal learning

performs well on caption generation

integrates easily with the **Transformers ecosystem.

3. Fine-Tuning Strategy

Instead of training the entire model from scratch, the project uses parameter-efficient fine-tuning with LoRA.

Benefits of LoRA:

reduces the number of trainable parameters

decreases GPU memory requirements

allows faster training

4. Training Process

The training pipeline involved:

Loading the pretrained BLIP model

Preparing image-caption pairs from the dataset

Applying LoRA adapters to attention layers

Training the model using the Hugging Face Trainer API

Saving the fine-tuned model

Uploading the model to Hugging Face

Training was performed using Google Colab with GPU acceleration.

5. Inference Pipeline

During inference:

The UI screenshot is passed to the processor

The image is encoded by the vision encoder

Cross-attention aligns visual features with text tokens

The decoder generates the caption sequentially

------------------------------------------------------------------------

## Assumptions

Several assumptions were made during the development of the model.

UI Screens Contain Recognizable Layout Patterns

The model assumes that UI screens follow common design patterns such as navigation bars, lists, buttons, and forms.

Screen-Level Captioning is Sufficient

The model generates captions for the entire screen, rather than describing each individual UI component.

Dataset Diversity is Adequate

The RICO dataset is assumed to contain sufficient variety in UI layouts and application types for the model to generalize.

Visual Context is Enough

The model assumes that meaningful captions can be generated from visual information alone, without additional metadata.

------------------------------------------------------------------------

## Observations

During training and inference, several observations were made.

1. The Model Learns UI Structure

The model is able to identify common UI elements such as:

navigation bars

lists

buttons

profile screens

and produce meaningful captions describing them.

2. Generic Captions for Complex Screens

For screens with many components, the model tends to produce more generalized captions rather than detailed descriptions.

Example:

Input: complex dashboard UI
Output:
“a mobile application interface with multiple options and icons”

3. Small Elements Are Hard to Detect

Very small UI elements such as icons or labels are sometimes ignored by the model.

4. Dataset Quality Affects Performance

The accuracy of captions strongly depends on the quality and diversity of training examples.

5. LoRA Significantly Reduces Training Cost

Using LoRA allowed fine-tuning the model with significantly fewer trainable parameters while maintaining good performance.

Summary

The project demonstrates that a pretrained vision-language model such as BLIP can be successfully adapted to the UI domain using parameter-efficient fine-tuning.

Despite limitations in detecting small elements, the model is able to generate meaningful captions for mobile UI screens and shows potential for applications in accessibility and automated UI documentation.

## Applications

UI Accessibility\
Generate descriptions for visually impaired users.

UI Search\
Search UI screenshots using natural language queries.

Automated Documentation\
Generate descriptions of application screens.

UI Design Analysis\
Understand layout patterns across apps.

------------------------------------------------------------------------

## Limitations

-   Complex layouts may produce generic captions
-   Small UI elements may be missed
-   Accuracy depends on training dataset diversity

------------------------------------------------------------------------

## Future Improvements

-   Component‑level UI captioning
-   Larger UI datasets
-   Multilingual caption generation
-   Real‑time UI analysis

------------------------------------------------------------------------

## Citation

    @misc{rico_ui_captioner,
    title={RICO UI Captioner: Vision-Language Model for UI Screen Captioning},
    author={Surabhi Muralidhar},
    year={2026},
    url={https://huggingface.co/surabhimuralidhar/rico-ui-captioner-final}
    }

------------------------------------------------------------------------

## Author

Surabhi Muralidhar

------------------------------------------------------------------------

## Acknowledgements

BLIP model research by Salesforce Research\
RICO dataset developed by Stanford University\
Model hosting by Hugging Face
