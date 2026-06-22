# import requests
# import pandas as pd

# url = "https://api.mfapi.in/mf/125497"

# response = requests.get(url)

# data = response.json()

# df = pd.DataFrame(data["data"])

# df.to_csv("data/raw/HDFC_Top100.csv",index=False)

# print(df.head())
import requests
import pandas as pd

funds = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, code in funds.items():

    print("Fetching", fund_name)

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    df.to_csv(f"data/raw/{fund_name}.csv", index=False)

    print(fund_name, "saved")