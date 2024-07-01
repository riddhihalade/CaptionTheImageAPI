from PIL import Image
import torch
from transformers import VisionEncoderDecoderModel, AutoTokenizer, ViTImageProcessor
from model_starter import model, feature_extractor, tokenizer, device, gen_kwargs

def image_to_text(image_paths):
    images = []
    for image_path in image_paths:
        image = image_path
        if image.mode != "RGB":
            image = image.convert(mode="RGB")
        images.append(image)

    inputs = feature_extractor(images=images, return_tensors="pt")
    pixel_values = inputs.pixel_values.to(device)

    # Generate attention_mask for pixel_values
    attention_mask = torch.ones(pixel_values.shape[:2], device=device)

    output_ids = model.generate(
        pixel_values,
        attention_mask=attention_mask,
        **gen_kwargs
    )

    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]

    return preds
