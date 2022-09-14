from tracemalloc import start
import pandas as pd
import math
import os
import glob

def delta(col, ind1, ind2=None):
    if ind2 == None:
        return col[ind1] - col[ind1-1]
    return col[ind1] - col[ind2]

def cleanData(df):
    # delete rows that have repeated values that are the same as the one right above. 
    try: 
        for index, row in df.iterrows():
            if row[1] == df.iloc[index-1][1] and row[2] == df.iloc[index-1][2]:
                df = df.drop(labels=index, axis=0)
    except:
        pass

def calculateRubine(df):
    cleanData(df)
    x_col = df.iloc[:, 1]
    y_col = df.iloc[:, 2]
    f8 = 0
    for i in range(1, df.shape[0], 1):
        f8 += math.sqrt(delta(x_col, i)**2 + delta(y_col, i)**2)
    return x_col, y_col, f8

def indexPoint(df, startX, startY):
    df[startX]

def resample():
    path = "resample-data/"
    csv_files = glob.glob(os.path.join(path, "*.csv"))
    for f in csv_files:
        df = pd.read_csv(f)
        x_col, y_col, length = calculateRubine(df)
        unit = length / 63
        for ind in range(64):
            # if unit is between some points, then interpolate the point between these two points, 
            # otherwise, index to next point and repeat the first step.
            
            for ()
            if unit * ind < 
            x_value = x_col[0] + unit * ind * (x_col[i] - x_col[i-1])
            y_value = y_col[0] + unit * ind * (y_col[i] - y_col[i-1])
        
if __name__ == "__main__":
    resample()