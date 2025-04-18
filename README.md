# 🧠 AI-Powered Resume Classifier

A Natural Language Processing (NLP) project that classifies resumes into job categories using lemmatization, text preprocessing, and machine learning techniques. Built with `spaCy`, `pandas`, and `scikit-learn`.

---

## 📌 Features

- Preprocesses raw resume text using spaCy (stopword removal, lemmatization)
- Adds a lemmatized resume column to the dataset
- Classifies resumes into job categories (e.g., HR, Data Science, Sales)
- Ready for model training using sklearn or any deep learning framework
- Optimized for performance using `tqdm` for progress tracking

---

## 📂 Dataset

The dataset used contains:

- `Resume_str`: Raw resume text
- `Category`: The actual category or department for the resume

Sample structure:

| Resume_str | Category |
|------------|----------|
| "The engineers are working efficiently..." | Engineering |

---

## 🔧 Installation

Clone the repository and install required libraries:

```bash
git clone https://github.com/aasiskndl/resume-classifier.git
cd resume-classifier

# Install dependencies
cd backend
pip install -r requirements.txt

# Download spaCy language model
python -m spacy download en_core_web_sm
```

## 🏷️ Label Examples
Some example resume categories:

- HR
- Data Science
- Sales
- Design
- Software Engineering
- Operations

## 🔮 Next Steps
- Vectorization using TF-IDF or Word Embeddings
- Train classification models (Logistic Regression, Random Forest, SVM, or deep learning)
- Build a web app to upload and classify resumes in real-time
- Deploy using Flask or Streamlit

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or improve.

## 🪪 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 💡 Author
Developed with ❤️ by Aashish
