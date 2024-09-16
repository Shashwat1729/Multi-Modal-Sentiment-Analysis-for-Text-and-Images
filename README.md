
# Multi-Modal Sentiment Analysis (Text + Images)

This project performs **multi-modal sentiment analysis** by analyzing both text and images in a social media post. It uses **BERT** for text sentiment and **ResNet** for image sentiment analysis, and combines both to give a final sentiment prediction.

## Features:
- Users can upload both text and images.
- The system analyzes the sentiment of both the text and image separately.
- Sentiment can be **Positive**, **Neutral**, or **Negative** for both modalities.

## Setup:

1. Clone this repository:
   ```bash
   git clone https://github.com/Shashwat1729/Multi-Modal-Sentiment-Analysis.git
   cd Multi-Modal-Sentiment-Analysis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000/` to upload text and images for sentiment analysis.

## Example Use Case:
- **Text Input**: "I love the new design of this product!"
- **Image Input**: An image of a smiling person or a beautiful product.
- The system will predict the sentiment for both text and image.

---

**Contributions**:
Feel free to contribute by opening issues or creating pull requests!
