"""
    Project description:
"""
import pandas as pd


def df_report(file_path):
    """

    :param file_path: File Path to the csv file of the data.
    :return: Creates a full report on the Data.
    """
    # Getting the name of the file, by separating the file_path at / and getting the last string from the list
    # created by the methode split.
    split_list = file_path.split("/")
    file_name = split_list[len(split_list) - 1]
    print("This is a Report on the Dataset" + "\033[1m", file_name + ".", "\033[0m")

    # Saving the Dataset in a global variable df.
    global df
    df = pd.read_csv(file_path)
    print("The Dataset is stored in the variable" + "\033[1m" + " df" + "\033[0m" + ".")
