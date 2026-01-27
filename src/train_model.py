import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

#Load dataset
df = pd.read_csv("data/instagram.csv")

#Fix column naming
df.rename(columns={"followes": "followers"}, inplace=True)

#Feature engineering
df["engagement_rate"] = (df["likes"] + df["comments"]) / df["followers"]

#Prepare data
X = df.drop("engagement_rate", axis=1)
y = df["engagement_rate"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#Models
lr = LinearRegression()
dt = DecisionTreeRegressor(max_depth=5, random_state=42)
rf = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)

#Train
lr.fit(X_train, y_train)
dt.fit(X_train, y_train)
rf.fit(X_train, y_train)

#Predict
lr_preds = lr.predict(X_test)
dt_preds = dt.predict(X_test)
rf_preds = rf.predict(X_test)

# Evaluate
print("Linear Regression MAE:", mean_absolute_error(y_test, lr_preds))
print("Decision Tree MAE:", mean_absolute_error(y_test, dt_preds))
print("Random Forest MAE:", mean_absolute_error(y_test, rf_preds))

# Save the best model (Random Forest in this case)
joblib.dump(rf, "models/random_forest_model.pkl")
print("Best model saved successfully.")