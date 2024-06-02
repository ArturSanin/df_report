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

    # Printing out the first 5 rows of the Dataset.
    print("To get a little overview on the data, here are the first 5 rows.")
    print(df.head())

    # Printing out the last 5 rows of the Dataset.
    print("Further here are the last 5 rows of the Data.")
    print(df.tail())

    # Printing out the Information of the Pandas shape methode.
    print("\033[1m" + "Dataset Shape Information" + "\033[0m")
    global df_number_rows, df_number_columns, df_number_entries, df_number_missing_entries
    df_number_rows = df.shape[0]
    df_number_columns = df.shape[1]
    df_number_entries = df.shape[0] * df.shape[1]
    df_number_missing_entries = df.isnull().sum().sum()
    print("The dataset has a total of:")
    print("   " + "\033[1m", df_number_rows,
          "rows." + "\033[0m" + " You can access on the number of rows through the variable " + "\033[1m" +
          "df_number_rows." + "\033[0m")
    print("   " + "\033[1m", df_number_columns,
          "columns." + "\033[0m" + " You can access on the number of columns through the variable " + "\033[1m" +
          "df_number_columns." + "\033[0m")
    print("   " + "\033[1m", df_number_entries,
          "entires." + "\033[0m" + " You can access on the number of entries through the variable " + "\033[1m" +
          "df_number_entries." + "\033[0m")
    print("   " + "\033[1m", df_number_missing_entries,
          "missing entries" + "\033[0m" +
          " in the whole dataset. You can access on the number of missing entries through the variable " + "\033[1m" +
          "df_number_missing_entries." + "\033[0m")
