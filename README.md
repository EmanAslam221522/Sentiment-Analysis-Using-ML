# 🎯 Sentiment Analysis on Movie Reviews

This project uses machine learning to predict whether a movie review is **Positive** or **Negative**. It uses TF-IDF vectorization and a logistic regression classifier to train and test on review data.

---

## 📂 Project Structure

- `sentiment_analysis.ipynb` – Jupyter notebook for training and testing the model.
- `model.pkl` – Trained sentiment classification model.
- `vectorizer.pkl` – TF-IDF vectorizer to convert text to numerical form.
- `app.py` – Script to test or predict new reviews using the saved model.
- `README.md` – Documentation and usage guide.

---

## 🚀 How to Run This Project

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. Install Dependencies

pip install -r requirements.txt

Run the Prediction Script

python app.py

Test it with Your Own Review!
Edit the review = "Your text here" line in app.py.

🧠 Model Information

    Algorithm: Logistic Regression

    Vectorization: TF-IDF

    Training Dataset: Sample movie reviews with labeled sentiments

📝 Example Review Predictions

review = "The plot made no sense and the acting was terrible."
# Output: ❌ Negative Review

review = "Absolutely loved the cinematography and performances!"
# Output: ✅ Positive Review

 Requirements

    Python 3.x

    scikit-learn

    pandas

    numpy



