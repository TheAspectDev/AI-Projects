import numpy as np
from sklearn import linear_model
from behtarin_dataset_jahan_by_yashar import numlist
        
x = np.array(numlist)
y = np.array([ 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2])

model = linear_model.LogisticRegression()
model.fit(x, y)

def predict(arr):
    prediction = model.predict(np.array(arr).reshape(1, -1))
    return prediction[0]
