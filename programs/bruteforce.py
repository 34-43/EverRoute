import pandas as pd

raw_path = "raw"
key_path = "keywords.txt"
excel_path = "에버랜드데이터셋11.xlsx"

def get_key_list(file_path : str):
    file = open(file_path,"r",encoding='utf-8')
    return file.read().split('\n')

def make_excel_2_csv(excel_path : str):
    csvpaths = []
    sheets = 3
    for i in range(sheets):
        excel_data = pd.read_excel(excel_path, sheet_name = i)
        excel_data.to_csv('exceldata_sheet'+ i + '.csv')
        csvpaths.append('exceldata_sheet'+ i + '.csv')
    return csvpaths

def main():
    key_list = get_key_list(key_path)
    csv_paths = make_excel_2_csv(excel_path)
    csv_data = pd.read_csv(csv_paths[0])
    print(key_list)
    key_list.index('사파리월드')
    print(csv_data.head())

main()