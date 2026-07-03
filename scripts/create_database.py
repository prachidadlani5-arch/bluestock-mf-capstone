from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

print("Database Created Successfully!") 