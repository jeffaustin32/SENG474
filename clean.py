#!/usr/bin/env python3
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LinearRegression

def main():
    filename = "data3.csv"
    headers = getheaders(filename)

    data = getdata(filename, headers)

    X,y = prepare(data, 3)

    #print(X)

    visualize_3d(X,y,headers[2],headers[3],headers[4])
    #Ptron(X, y)
    #svmclass(X,y)
    #Lregress(X, y)

def Lregress(X, y):
    reg = LinearRegression().fit(X,y.ravel())
    print(reg.score(X,y))

def Ptron(X, y):
    clf = Perceptron(tol=1e-3, random_state=0)
    clf.fit(X,y.ravel())
    print(clf.score(X,y))

def svmclass(X,y):
    clf = svm.SVC(gamma = 0.001, C=100)
    clf.fit(X[:-1],y[:-1].ravel())
    result = clf.predict(X)

    match = 0
    for num in range (len(result)):
        if(result[num] == y[num]):
             match = match + 1
    print("Percent matching: " + str(match/len(result)))

def getdata(filename, headers):
    data = pd.read_csv(filename, header=None, names = headers)
    data.head()
    data = data.drop(data.index[0])     #Drop header text
    data = data.astype('float64')       #Convert to float
    data.insert(0, "winner", 0) #Insert column for comparison
    return data

#numattr is the number of columns for your classification
def prepare(data, numattr):
    #Compare the percent of votes for each candidate and insert into winner column
    data.loc[data['trump'] > data['clinton'], "winner"] = 0 #Trump
    data.loc[data['clinton'] > data['trump'], "winner"] = 1 #Clinton

    #print(data)

    X = data.iloc[:,3:3+numattr].values #Get last two columns
    y = data.iloc[:,0:1].values #Get first two columns #Clinton-Trump

    X = np.insert(X, 0, 1, axis=1)

    # we build a boolean index
    where_are_zeros = (y==0)
    y[where_are_zeros] = -1

    return X,y

#Create 2D visualization of data
def visualize_2d(X, y, col1, col2):
    positive_indexes = np.where(y == 1)[0]  #Clinton
    negative_indexes = np.where(y == -1)[0] #Trump

    positive = X[positive_indexes]  # positive rows
    negative = X[negative_indexes]  # negative rows

    #print(negative)

    fig, ax = plt.subplots(figsize=(12,8))
    ax.scatter(positive[:,1:2], positive[:,2:], s=50, c='b', marker='o', label='Clinton')
    ax.scatter(negative[:,1:2], negative[:,2:], s=50, c='r', marker='x', label='Trump')
    ax.legend()
    ax.set_xlabel('%'+col1)
    ax.set_ylabel('%'+col2)

    plt.show()

#Create 3D visualization of data
def visualize_3d(X, y, col1, col2, col3):
    positive_indexes = np.where(y == 1)[0]  #Clinton
    negative_indexes = np.where(y == -1)[0] #Trump

    positive = X[positive_indexes]  # positive rows
    negative = X[negative_indexes]  # negative rows

    #print(positive[:,3:])
    #print(negative)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(positive[:,1:2], positive[:,2:3], positive[:,3:], s=50, c='b', marker='o', label='Clinton')
    ax.scatter(negative[:,1:2], negative[:,2:3], negative[:,3:], s=50, c='r', marker='x', label='Trump')
    ax.legend()
    ax.set_xlabel(col1)
    ax.set_ylabel(col2)
    ax.set_zlabel(col3)

    plt.show()

#Strip the first line from the input .csv file
def getheaders(filename):
    with open(filename) as infile:
        first_line = infile.readline()

    result = [x.strip() for x in first_line.split(',')]
    return result

if __name__ == "__main__":
    main()
