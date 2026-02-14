import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("instagram_data.csv")

print(df.head())
print(df.info())

# Create Engagement Rate if not present
if "engagement_rate" not in df.columns:
    df["engagement_rate"] = (df["likes"] + df["comments"]) / df["followers"]

# Followers vs Likes
plt.scatter(df["followers"], df["likes"])
plt.xlabel("Followers")
plt.ylabel("Likes")
plt.title("Followers vs Likes")
plt.show()

# Engagement Rate Distribution
plt.hist(df["engagement_rate"], bins=30)
plt.xlabel("Engagement Rate")
plt.ylabel("Frequency")
plt.title("Engagement Rate Distribution")
plt.show()

# Likes vs Comments
plt.scatter(df["likes"], df["comments"])
plt.xlabel("Likes")
plt.ylabel("Comments")
plt.title("Likes vs Comments")
plt.show()
