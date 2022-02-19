import pytest
import os
import pandas as pd
from scorewithimage import _visualize

def test_visualize():
    df = pd.DataFrame({
        "image": [],
        "score": [],
    })
    assert _visualize(df).find("html") > -1

    df = pd.DataFrame({
        "image": [__file__],
        "score": [0.99],
    })
    assert _visualize(df).find("html") > -1

    json_ = f'[{{ "image": "{__file__}", "score": 0.99 }}]'
    assert _visualize(df).find(f'<div id="items-data">') > -1

def test_visualize_score_column_must_be_numeric():
    df = pd.DataFrame({
        "image": ["/hoge.jpg"],
        "score": ["a"],
    })
    
    with pytest.raises(ValueError):
        _visualize(df)

def test_visualize_image_column_must_be_string():
    df = pd.DataFrame({
        "image": [1],
        "score": [1],
    })
    
    with pytest.raises(ValueError):
        _visualize(df)

def test_visualize_image_column_must_be_existing_filepath():
    df = pd.DataFrame({
        "image": ["/hoge.jpg"],
        "score": [1],
    })
    
    with pytest.raises(FileNotFoundError):
        _visualize(df)

def test_visualize_you_must_have_image_and_score_column():
    df = pd.DataFrame({
        "image": [],
    })
    
    with pytest.raises(ValueError):
        _visualize(df).find("html")
    
    df = pd.DataFrame({
        "score": [],
    })
    
    with pytest.raises(ValueError):
        _visualize(df).find("html")