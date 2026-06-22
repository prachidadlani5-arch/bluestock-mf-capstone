import pandas as pd
import os

folder = "data/raw"

files = os.listdir(folder)

for file in files:

    if file.endswith(".csv"):

        print("\n"+"="*50)
        print("File:", file)

        df = pd.read_csv(os.path.join(folder,file))

        print("\nShape:")
        print(df.shape)

        print("\nDatatypes:")
        print(df.dtypes)

        print("\nFirst 5 rows:")
        print(df.head())