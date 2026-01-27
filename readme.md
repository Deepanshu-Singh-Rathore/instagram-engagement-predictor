📊 Instagram Influencer Engagement Predictor
📌 Overview

This project predicts the engagement rate of Instagram influencers using Machine Learning.
Rather than relying solely on follower count, the model helps identify influencers with genuinely high engagement.

Engagement Rate Formula:
(likes + comments) / followers

🎯 Objectives

Analyze Instagram influencer metrics

Perform feature engineering

Train and compare regression models

Evaluate models using standard regression metrics

Select the best-performing model

🧠 Machine Learning Approach

Problem Type: Regression

Target Variable: Engagement Rate

Models Implemented

Linear Regression

Decision Tree Regressor

Random Forest Regressor

📊 Results
Model	MAE
Linear Regression	0.131
Decision Tree	0.033
Random Forest	0.031

✅ Random Forest Regressor achieved the lowest MAE and was selected as the final model.

🗂 Project Structure
instagram-engagement-predictor/
│
├── data/              # Dataset files
├── src/               # Training and preprocessing scripts
├── models/            # Saved trained models
├── notebooks/         # EDA and experiments
├── README.md          # Project documentation
├── requirements.txt   # Dependencies
└── .gitignore

🚀 How to Run the Project

1. Clone the repository:

git clone https://github.com/Deepanshu-Singh-Rathore/instagram-engagement-predictor.git
cd instagram-engagement-predictor

2. Install dependencies:

pip install -r requirements.txt

3. Train the model:

python src/train_model.py

👥 Team Contributions

Me: Feature engineering, model training, evaluation, and final model selection

Partner: Dataset preparation, exploratory data analysis (EDA), baseline modeling, and visualization

🔮 Future Improvements

Engagement category classification (Low / Medium / High)

Incorporation of content-based features (hashtags, captions, post type)

Use of advanced models (XGBoost, LightGBM)

Model deployment using Streamlit or FastAPI