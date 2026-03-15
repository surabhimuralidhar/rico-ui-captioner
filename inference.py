from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests
from io import BytesIO


MODEL_NAME = "surabhimuralidhar/rico-ui-captioner-final"


def load_model():
    processor = BlipProcessor.from_pretrained(MODEL_NAME)
    model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME)
    return processor, model


def load_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content)).convert("RGB")
    return image


def generate_caption(processor, model, image):
    inputs = processor(images=image, return_tensors="pt")
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption


def main():
    processor, model = load_model()

    image_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/coco_sample.png"

    image = load_image(image_url)

    caption = generate_caption(processor, model, image)

    print("\nGenerated Caption:")
    print(caption)


if __name__ == "__main__":
    main()
