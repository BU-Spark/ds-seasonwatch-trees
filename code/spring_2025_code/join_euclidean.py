import pandas as pd
from scipy.spatial import cKDTree


def join_euclidean(df1, df2, df1_xy_cols, df2_xy_cols, data_col):
    """performs a join on minimum euclidean distance"""
    tree = cKDTree(df1[df1_xy_cols].values)
    distances, indices = tree.query(df2[df2_xy_cols].values)
    nearest = df1.iloc[indices][data_col].reset_index(drop=True)

    return pd.concat([df2.reset_index(drop=True), nearest], axis=1)
