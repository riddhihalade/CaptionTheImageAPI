from transformers import VisionEncoderDecoderModel, AutoTokenizer, ViTImageProcessor
import torch

# Load models and tokenizer
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

# Device configuration
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Generation parameters
max_length = 16
num_beams = 4
gen_kwargs = {
    "max_length": max_length,
    "num_beams": num_beams,
    "pad_token_id": tokenizer.pad_token_id
}
