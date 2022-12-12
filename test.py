import joblib
import pytest

def load_model():
    return joblib.load('regression.joblib')



def test_model():
    model = load_model()

    size = [205,186,187,83]
    room = [2,2,1,2]
    garden = [0,0,1,1]
    price = [212533.42002884124,198905.51100435725,264370.41342138103,226599.7389458302]
    for i in range (len(size)):
        X = [[size[i], room[i], garden[i]]]
        test_price = model.predict(X)
        assert test_price == price[i]
        print(test_price, price[0])





