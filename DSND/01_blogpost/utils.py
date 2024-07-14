import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

def find_optimal_lm_mod(df, cutoffs, col_price, prices, test_size = .30, random_state=42):
    '''
    INPUT
    df - pandas dataframe, to be used for modeling
    cutoffs - list of ints, cutoff for number of non-zero values in dummy categorical vars
    col-price - name of the column with the price to be modeled
    prices - list of ints, max price that shall be considered for modeling
    test_size - float between 0 and 1, default 0.3, determines the proportion of data as test data
    random_state - int, default 42, controls random state for train_test_split

    OUTPUT
    df_res - pandas dataframe with the r2 score for test and train data and the number of features  in dependency of the cutoff, the maximum price
    '''
    cutoff_list, num_feats_list, price_list, r2_score_test_list, r2_score_train_list, df_res = [], [], [], [], [], pd.DataFrame
  
    for cutoff in cutoffs:

        print('Caclculation started for cutoff ' +str(cutoff))

        # reduce matrix
        df_f = df.iloc[:, np.where((df.sum() > cutoff) == True)[0]]

        for price in prices:

            # filter accordung to the max price
            df_ff = df_f[df_f[col_price] < price]

            # split the variables
            X = df_ff.drop(columns=col_price)
            y = df_ff[col_price]


            #split the data into train and test
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state=random_state)

            #fit the model and obtain pred response
            lm_model = LinearRegression()
            lm_model.fit(X_train, y_train)
            y_test_preds = lm_model.predict(X_test)
            y_train_preds = lm_model.predict(X_train)

            # append values to lists
            price_list.append(price)
            cutoff_list.append(cutoff)
            num_feats_list.append(X.shape[1])
            r2_score_test_list.append(r2_score(y_test, y_test_preds))
            r2_score_train_list.append(r2_score(y_train, y_train_preds))



    df_res = pd.DataFrame({
        'price': price_list,
        'cutoff': cutoff_list,
        'num_features': num_feats_list,
        'r2_score_test': r2_score_test_list,
        'r2_score_train': r2_score_train_list})



    return df_res

