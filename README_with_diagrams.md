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
    ├── train.ipynb
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

"A mobile application interface displaying multiple options and icons."

------------------------------------------------------------------------

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
