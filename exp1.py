import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
data = {
    "gender": ["Male", "Female", "Male", "Female"],
    "age": [20, 22, None, 24],
    "bmi": [22, 25, 24, None],
    "HbA1c_level": [5.2, 5.6, None, 6.1],
    "diabetes": [0, 0, 1, 0]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)
df["age"] = df["age"].fillna(df["age"].mean())
df["bmi"] = df["bmi"].fillna(df["bmi"].mean())
df["HbA1c_level"] = df["HbA1c_level"].fillna(df["HbA1c_level"].mean())
df = df.drop_duplicates()
le = LabelEncoder()
df["gender"] = le.fit_transform(df["gender"])
scaler = MinMaxScaler()
df[["age", "bmi", " HbA1c_level"]] = scaler.fit_transform(
    df[["age", "bmi", "HbA1c_level"]]
)
df.to_csv("output.csv", index=False)
print("\nProcessed Data:")
print(df)
print("\nPreprocessing completed!")
