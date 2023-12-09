import pandas as pd
import os as os
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



def make_days_2_date(days):
    return pd.to_datetime(days,unit='D',origin='1899-12-30').date()

def is_wd_equal(date1,date2):
    return date1.weekday() == date2.weekday()

def get_wd_df(df,clock):
    return df[df.apply(lambda row: is_wd_equal(make_days_2_date(row['날짜']),clock),axis=1)]

def get_await_time(df,clock,target : str):
    df_wd = get_wd_df(df,clock)
    h = clock.hour
    # if clock.minute < 30: h -= 1
    if h < 10 or h >18: return -1
    new = dt.time(hour=h,minute=30)
    row_of_new = df_wd.iloc[:,2][df_wd.iloc[:,2]==str(new)].index.to_list()[0]
    return df.loc[row_of_new,target]

def get_route_time(df,start,end):
    row_of_start = df.iloc[:,1][df.iloc[:,1]==start].index.to_list()[0]
    return df.loc[row_of_start,end]

def maximum_rides(df_aw,df_rt):
    pass

#------ down : main ------

def main():
    csv_paths = get_csv_paths(sheets)
    df_await = read_csv(csv_paths[0])
    df_route1 = read_csv(csv_paths[1])
    df_route2 = read_csv(csv_paths[2])
    key_list = df_await.columns[3:].to_list()
    # toggle for reloading raw files
    update = False
    if update: make_excel_2_csv(excel_p,csv_paths)
    if update: write_key(key_list)
    # use -----------------------------------
    df_route = df_route2
    basetime = dt.datetime.today()

    print(get_route_time(df_route,'사파리월드','릴리댄스'))
    print(get_await_time(df_await,basetime,'슈팅고스트'))
    print(get_await_time(df_await,dt.datetime(2023,11,23,16,00,0),'피터팬'))

main()