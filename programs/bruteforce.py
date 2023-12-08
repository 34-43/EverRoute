import pandas as pd
import os as os
from enum import Enum, auto
import datetime as dt

raw_p = "raw"
parsed_p = "parsed"
excel_p = "에버랜드데이터셋11_static.xlsx"
sheets = 3
csv_p = "exceldata_sheet"
key_p = "keywords.log"

def make_path(dir_p,file_p):
    return os.path.join(os.getcwd(),dir_p,file_p)

def get_csv_paths(count):
    csvpaths = []
    for i in range(count):
        csvpaths.append('exceldata_sheet'+ str(i) + '.csv')
    return csvpaths

def make_excel_2_csv(excel_p : str, csvpaths : list):
    for i in range(len(csvpaths)):
        excel_data = pd.read_excel(make_path(raw_p,excel_p), sheet_name = i)
        excel_data.to_csv(make_path(parsed_p,csvpaths[i]))

def read_csv(csv_path):
    return pd.read_csv(make_path(parsed_p,csv_path))

def write_key(key_list):
    file = open(make_path(parsed_p,key_p),"w",encoding='utf-8')
    for key in key_list:
        file.write(key + "\n")

def create_enum(values):
    return Enum('',{value: auto() for value in values})

def make_days_2_date(days):
    return pd.to_datetime(days,unit='D',origin='1899-12-30')

def get_await_time(df,datetime,target):
    dt.datetime.today()
    pass

def get_route_time(df,start,end):
    #row_of_start = first column's row index of start value
    row_of_start = df.iloc[:,1][df.iloc[:,1]==start].index.to_list()[0]
    return df.loc[row_of_start,end]

def weekday_condition(row):
    return make_days_2_date(row['날짜']).weekday() < 4

#------ down : main ------

def main():
    # toggle for reloading raw files
    update = False
    # parse & store excel
    csv_paths = get_csv_paths(sheets)
    if update: make_excel_2_csv(excel_p,csv_paths)
    # read from stored csv
    df_await = read_csv(csv_paths[0])
    df_route1 = read_csv(csv_paths[1])
    df_route2 = read_csv(csv_paths[2])
    # parse & store key
    key_list = df_await.columns[3:].to_list()
    if update: write_key(key_list)
    # create enum
    R = create_enum(key_list)
    # use -----------------------------------
    # current using dataframe
    df_route = df_route2
    print(get_route_time(df_route,'사파리월드','사파리월드'))
    print(get_route_time(df_route,'썬더폴스','우주전투기'))
    print(get_route_time(df_route,'사파리월드','플라잉레스큐'))
    print(make_days_2_date(45252))
    print(make_days_2_date(45257))
    print(make_days_2_date(45258))
    # var = df_await[df_await.apply(weekday_condition,axis=1)]
    # print(var)

main()