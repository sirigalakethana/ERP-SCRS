import pandas as pd

def save_students(data):
    df = pd.DataFrame(data)
    df.to_csv("data/students.csv", index=False)

def load_students():
    return pd.read_csv("data/students.csv")