import pandas as pd
from titanic_mlops.model import train

def test_train_predict_length():
    df = pd.DataFrame({
        "Survived": [0, 1, 0, 1],
        "Pclass": [3, 1, 2, 3],
        "Sex": [0, 1, 0, 1],
        "Age": [22, 38, 26, 35],
        "Fare": [7.25, 71.28, 8.05, 53.10]
    })
    model = train(df)
    preds = model.predict(df.drop("Survived", axis=1))
    assert len(preds) == len(df)
