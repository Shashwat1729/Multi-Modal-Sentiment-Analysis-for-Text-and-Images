import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torchvision import models, transforms
from PIL import Image

# Load pre-trained BERT model for text sentiment analysis
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
text_model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)

# Load pre-trained ResNet model for image sentiment analysis
image_model = models.resnet50(pretrained=True)
image_model.fc = torch.nn.Linear(image_model.fc.in_features, 3)  # Adjust for 3 classes (positive, neutral, negative)

# Image transformations for ResNet
image_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Function for text sentiment analysis
def analyze_text_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)
    outputs = text_model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=1)
    sentiment = ['Negative', 'Neutral', 'Positive'][predictions.item()]
    return sentiment

# Function for image sentiment analysis
def analyze_image_sentiment(image_path):
    image = Image.open(image_path).convert('RGB')
    image = image_transforms(image).unsqueeze(0)
    
    with torch.no_grad():
        outputs = image_model(image)
    predictions = torch.argmax(outputs, dim=1)
    sentiment = ['Negative', 'Neutral', 'Positive'][predictions.item()]
    return sentiment
