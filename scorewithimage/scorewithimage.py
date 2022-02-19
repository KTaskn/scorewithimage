import os
import pandas as pd
from pandas.api.types import is_numeric_dtype, is_string_dtype

def _visualize(df: pd.DataFrame):
    __check_columns_name(df)
    __check_columns_type(df)
    __check_files_exist(df)

    val_text = f'<div id="items-data">{df.to_json(orient="records")}</div>'
    print(val_text)
    with open(os.path.join(os.path.dirname(__file__), "index.html")) as f:
        html = f.read()
        return f"{val_text}{html}"

def __check_columns_name(df: pd.DataFrame):
    if "score" in df.columns and "image" in df.columns:
        return True
    else:
        raise ValueError("you must have a 'score' and 'image' column")

def __check_columns_type(df: pd.DataFrame):
    if df.__len__() == 0:
        return True
    else:
        if is_numeric_dtype(df["score"]):
            if is_string_dtype(df["image"]):
                return True
            else:
                raise ValueError("'image' column must be string")
        else:
            raise ValueError("'score' column must be numeric")

def __check_files_exist(df: pd.DataFrame):
    flags = df["image"].map(os.path.exists)
    if df["image"].map(os.path.exists).all():
        return True
    else:
        raise FileNotFoundError(f"file not found: {df['image'][flags == False]}")