import pandas as pd
import openpyxl
import os
from tkinter import filedialog
import tkinter as tk
from tkinter.filedialog import askopenfilename


def import_csv_data():
    global v
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    df = pd.read_csv(csv_file_path)
    dir_name = filedialog.askdirectory()  # asks user to choose a directory
    os.chdir(dir_name)  # changes your current directory
    df.to_excel('ExcelDataFrame.xlsx', index=False)

    df = pd.read_excel('ExcelDataFrame.xlsx')
    df['Date'] = pd.to_datetime(df['Date'])

    # data mapping for day of the week
    # MAPPING

    dw_mapping = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    df['Day'] = df['Date'].dt.dayofweek.map(dw_mapping)
    df['Range Close/Open'] = df[' Close'] / df[' Open'] - 1

    df.to_excel('ExcelDataFrame.xlsx', index=False)

root = tk.Tk()
tk.Label(root, text='File Path').grid(row=0, column=0)
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v).grid(row=0, column=1)
tk.Button(root, text='Browse Data Set and save in cd',command=import_csv_data).grid(row=1, column=0)
tk.Button(root, text='Close',command=root.destroy).grid(row=1, column=1)
root.mainloop()
