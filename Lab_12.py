import numpy as np
import pandas as pd
import sklearn as skl
from sklearn.model_selection import train_test_split 
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
plt.style.use('ggplot')

from sklearn.datasets import load_iris
iris = load_iris()
#print(iris.data)

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

training = pd.DataFrame(data=X_train, columns=iris.feature_names)

shapes = [(1),(100,100),(100,90,80,70,60),(20,60),(1,1,1,1,1,1,1,1),(5,10,15,20),(25,75,25),(10,10,10,10),(1,5,10,5,1),(50)]

for layer in shapes:
    print("Using hidden layer with the shape of : "+str(layer))
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=layer, random_state=1)
    clf.fit(X_train,y_train)
    print("Accuraccy score:", clf.score(X_test,y_test))