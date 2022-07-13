# logistic regression

# import the class
from sklearn.linear_model import LogisticRegression

def logreg(folder):

    feature_cols = ['Elo', 'Goal_Difference', 'Home_away']

    X = folder[feature_cols] # Features
    y = folder['labelwin'] # Target variable

    # instantiate the model (not using the default parameters because it is "crashing" otherwise)
    lr = LogisticRegression(max_iter=3000)

    # fit the model with data
    lr.fit(X, y)

    #feature_cols = ['Income', 'Limit', 'Rating', 'Cards','Age','Education']
    

    y_pred = lr.predict_proba(X_pred1)
    y_pred = lr.predict_proba(X_pred2)