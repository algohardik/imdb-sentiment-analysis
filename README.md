# IMDB Sentiment Analysis App

A deep learning-based web app for analyzing the sentiment of movie reviews using the IMDB dataset. This project uses a regularized CNN-based architecture to classify reviews as positive or negative.

---

## 🧠 Model Architecture

```python
model = Sequential([
    Input(shape=(500,)),
    Embedding(10000, 128),

    Conv1D(64, 5, padding='same'),
    BatchNormalization(),
    LeakyReLU(),

    Conv1D(64, 5, padding='same'),
    BatchNormalization(),
    LeakyReLU(),

    GlobalMaxPooling1D(),

    Dense(64, kernel_regularizer=l2(0.01)),
    LeakyReLU(),
    Dropout(0.6),

    Dense(1, activation='sigmoid')
])


## 📁 Folder Structure
```
.
├── app.py                    # Streamlit application
├── model
│   └── sentiment_model.keras  # Trained deep learning model
├── movie_review_sentiment.ipynb  # Jupyter notebook for training
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

```

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📦 Requirements
- Python >= 3.8
- TensorFlow >= 2.12
- Streamlit

## 📝 Sample Output
```
Review: "This movie is good"

🧼 Cleaned Review:
this movie is good

🔎 Token Mapping:
        this → 14
       movie → 20
          is → 9
        good → 52

📦 Padded Review Shape: (1, 500)

📊 Predicted Sentiment: Positive (Probability: 0.7265)
(np.float32(0.7265019), 'Positive')

```