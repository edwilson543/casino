import pandas as pd


def get_wheel_defn_dict(filename: str,
                        number_column: str,
                        colour_column: str) -> dict:
    """
    Purpose:
    --------
    If we want to define some custom roulette wheels via a csv file

    Parameters:
    -----------
    filename: the name of the file we are reading (from the same folder)
    number_column: the column with the associated roulette wheel number in it
    colour_column: the colour of that number on the roulette wheel

    Return:
    -------
    A dictionary that maps each number of the roulette wheel from the csv file onto a specific number
    """
    defn_df = load_wheel_defn(filename, number_column)
    defn_ser = wheel_defn_df_to_ser(defn_df, colour_column)
    defn_dict = wheel_defn_ser_to_dict(defn_ser)
    return defn_dict


def load_wheel_defn(filename: str, colour_column: str) -> pd.DataFrame:
    return pd.read_csv(filename + '.csv', index_col=colour_column)


def wheel_defn_df_to_ser(defn_dataframe: pd.DataFrame, colour_column) -> pd.Series:
    return pd.Series(defn_dataframe[colour_column], index=defn_dataframe.index)


def wheel_defn_ser_to_dict(defn_ser: pd.Series) -> dict:
    return defn_ser.to_dict()
