
# 🎯 Sentiment Analysis on Movie Reviews

This project applies **Machine Learning** techniques to automatically determine the **sentiment** (Positive or Negative) of movie reviews. It uses **TF-IDF vectorization** to extract textual features and a **Logistic Regression model** for classification.

The project demonstrates how natural language processing (NLP) can be used to understand emotions and opinions expressed in text, which is a fundamental task in various applications like recommendation systems, feedback analysis, and social media monitoring.

---

## 📘 Table of Contents

1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Model Details](#model-details)
6. [Example Predictions](#example-predictions)
7. [Dependencies](#dependencies)
8. [Future Improvements](#future-improvements)
9. [License](#license)

---

## 🔍 Overview

The **Sentiment Analysis on Movie Reviews** project is designed to classify text reviews as **Positive** or **Negative** using machine learning. It trains a model on labeled data containing movie reviews and their respective sentiments.

The steps involved include:

* Data preprocessing (cleaning and tokenizing text)
* Feature extraction using **TF-IDF**
* Model training using **Logistic Regression**
* Saving and reusing the trained model for prediction

---

## 📂 Project Structure

```
├── sentiment_analysis.ipynb   # Jupyter notebook for training & evaluation  
├── model.pkl                  # Trained sentiment classification model  
├── vectorizer.pkl             # TF-IDF vectorizer for text feature extraction  
├── app.py                     # Script to make predictions on new reviews  
├── requirements.txt           # Python dependencies  
└── README.md                  # Project documentation  
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate       # On macOS/Linux
venv\Scripts\activate          # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Run the Jupyter Notebook

To view the training process and evaluate model performance:

```bash
jupyter notebook sentiment_analysis.ipynb
```

### 2. Run the Prediction Script

To test the model with new reviews:

```bash
python app.py
```

### 3. Test with Your Own Review

In the `app.py` file, locate the line:

```python
review = "Your text here"
```

Replace `"Your text here"` with your own review text, save the file, and rerun the script.

The program will output whether the sentiment is **Positive ✅** or **Negative ❌**.

---

## 🧠 Model Details

| Parameter              | Description                                                    |
| ---------------------- | -------------------------------------------------------------- |
| **Algorithm**          | Logistic Regression                                            |
| **Feature Extraction** | TF-IDF (Term Frequency - Inverse Document Frequency)           |
| **Dataset**            | Movie reviews labeled as positive or negative                  |
| **Accuracy**           | Achieved high accuracy on test data (based on dataset quality) |

**How it works:**

1. The **TF-IDF vectorizer** converts text into numerical features by calculating how important a word is in relation to the document and corpus.
2. The **Logistic Regression model** then learns patterns between these features and the sentiment labels during training.
3. The trained model and vectorizer are saved using **pickle (.pkl)** for quick reuse during prediction.

---

## 📝 Example Predictions

```python
# Example 1
review = "The plot made no sense and the acting was terrible."
# Output: ❌ Negative Review

# Example 2
review = "Absolutely loved the cinematography and performances!"
# Output: ✅ Positive Review
```

---

## 📦 Dependencies

Ensure the following packages are installed (already included in `requirements.txt`):

* Python 3.x
* scikit-learn
* pandas
* numpy
* pickle (built-in)

Install all with:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

* Add **Deep Learning models** (e.g., LSTM, BERT) for better accuracy
* Integrate a **Flask or FastAPI web interface** for user input
* Expand dataset for multilingual or domain-specific reviews
* Include **visualizations** for word frequency and model performance

---

## 📜 License

This project is open-source and available under the **MIT License**.
You are free to use, modify, and distribute it for educational or research purposes.


