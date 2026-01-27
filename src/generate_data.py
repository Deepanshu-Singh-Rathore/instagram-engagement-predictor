import pandas as pd
import numpy as np


np.random.seed(42)

num_rows = 1000

data = {
    "followers": np.random.randint(1_0000,1_000_000, num_rows),
    "likes": np.random.randint(50, 50_000, num_rows),
    "comments": np.random.randint(5, 5_000, num_rows),
    "posts": np.random.randint(10, 2_000, num_rows),
    "following": np.random.randint(100, 5000, num_rows),
    "is_verified": np.random.choice([0, 1], num_rows),
}
df = pd.DataFrame(data)

df = pd.DataFrame(data)

df.to_csv("data/instagram.csv", index=False)

print("Dataset created successfully!")
print(df.head())
