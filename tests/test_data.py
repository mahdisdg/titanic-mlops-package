import pandas as pd
from titanic_mlops.data import load_and_clean

def test_cleaned_columns(tmp_path):
    df = pd.DataFrame({
        "Survived": [1, 0],
        "Pclass": [1, 3],
        "Sex": ["male", "female"],
        "Age": [22, 38],
        "Fare": [7.25, 71.28]
    })
    file = tmp_path / "data.csv"
    df.to_csv(file, index=False)
    clean = load_and_clean(str(file))
    assert "Sex" in clean.columns
    assert set(clean["Sex"].unique()) == {0, 1}
