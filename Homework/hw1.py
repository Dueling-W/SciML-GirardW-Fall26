import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from sklearn.model_selection import train_test_split

def build_matrix(M, t_values):

    df2 = pd.DataFrame(columns=[list(range(0, M+1))])

    for t in t_values:

        row = []
        for i in range(M+1):
            t_pow = pow(t, i)
            row.append(t_pow)

        df2.loc[len(df2)] = row
        row.clear()

    return df2
        


        

if __name__ == "__main__":


    df = pd.read_csv('Homework/hw1.csv') # load from within homework folder

    t_values = df['0'].values.tolist()

    df2 = build_matrix(3, t_values)

    matrix_A = np.array(df2)
    print(matrix_A)

    coeff = np.linalg.lstsq(matrix_A, df[' 1'])[0]

    print(coeff)

    print(coeff[2])

    plt.plot(df['0'], df[' 1'], 'o', label='Original data', markersize=10)
    plt.plot(df['0'], coeff[0]*pow(df['0'], 3) + coeff[1]*pow(df['0'], 2) + coeff[2]*df['0'] + coeff[3], 'r', label='Fitted line')
    plt.legend()
    plt.show()






    