import pandas as pd

key_path = "keywords.txt"
excel_path = "에버랜드데이터셋11.xlsx"

def get_key_list(file_path : str):
    file = open(file_path,"r",encoding='utf-8')
    return file.read().split('\n')

def main():
    key_list = get_key_list(key_path)
    excel_data = pd.read_excel(excel_path, sheet_name = 0)
    print(key_list)
    key_list.index('사파리월드')
    print(excel_data.head())

main()