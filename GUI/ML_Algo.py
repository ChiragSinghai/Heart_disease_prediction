import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

df=pd.read_csv('Heart.csv')
X,Y=df.loc[:,:'thal'],df['target']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)       
class Algorithms():
    def __init__(self):
        self.dt=DecisionTreeClassifier()
        self.dt.fit(X_train,Y_train)
        self.sc=StandardScaler().fit(X)
        X_train_std=self.sc.transform(X_train)
        X_test_std=self.sc.transform(X_test)
        self.knn=KNeighborsClassifier(n_neighbors=4)
        self.knn.fit(X_train_std,Y_train)
        self.logreg = LogisticRegression() 
        self.logreg.fit(X_train_std, Y_train) 
        self.dt1=DecisionTreeClassifier()
        self.dt1.fit(X_train.drop('fbs',axis=1),Y_train)

    def getAccuracy(self,model,X_tester,Y_tester):
        prediction=model.predict(X_tester)
        accuracy_dt=accuracy_score(Y_tester,prediction)*100
        return accuray_dt

    def inside_prediction(self,model,L):
        return model.predict(L)

    def prediction(self,L):
        L_std=self.sc.transform(np.array([L]))
        A=L[0:5]+L[6:]
        algo=[(self.dt,np.array([L])),(self.dt1,np.array([A])),
              (self.knn,L_std),(self.logreg,L_std)]
        
        s=0
        for i in algo:
            s+=(self.inside_prediction(i[0],i[1]))
        return 1 if s>=2 else 0
    
if __name__=='__main__':
    L=[63 ,1, 3,145,233,1,0,150,0,2.3,0,0,1]
    obj=Algorithms()
    
    print(obj.prediction(L))
    
    
    
        

