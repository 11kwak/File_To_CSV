import os
import pandas as pd
from tqdm import tqdm

class Tocsv:
    def __init__(self,file_list,csv_name):
        self.file_list = file_list
        self.csv_name = csv_name
        self.exceltocsv = self.exceltocsv()
        self.txttocsv = self.txttocsv()
        self.csvtocsv = self.csvtocsv()


        
    def tocsv(self):
        file_list = os.listdir('rawdata')
        csv_name = ""
        for name in tqdm(file_list):
            src = os.path.splitext(name) #확장자 분리
            csv_name = src[0]+'.csv'     #csv 붙여서 이름 만들기
            if src[1] == ".xlsx":
                test_df = pd.read_excel("rawdata/{0}".format(name))
                test_df.to_csv("csvdata/{0}".format(csv_name),header=False,index=False,encoding="cp949")
                self.exceltocsv

            elif src[1] == ".xls":
                test_df = pd.read_excel("rawdata/{0}".format(name))
                test_df.to_csv("csvdata/{0}".format(csv_name),header=False,index=False,encoding="cp949")
                self.exceltocsv
                

            elif src[1] == ".TXT":
                test_df = pd.read_table("rawdata/{0}".format(name), sep = "|")
                test_df.to_csv("csvdata/{0}".format(csv_name),header=False,index=False,encoding="cp949")
                self.txttocsv

            elif src[1] == ".csv":
                test_df = pd.read_csv("rawdata/{0}".format(name), encoding='utf-8')
                test_df.to_csv("csvdata/{0}".format(csv_name),header=False,index=False,encoding='cp949')
                self.txttocsv

            else:
                print("Only xlsx, txt, csv file plz")


    def exceltocsv(self):
        print("엑셀을 csv로 만듭니다.")

    def txttocsv(self):
        print("txt파일을 csv로 만듭니다.")

    def csvtocsv(self):
        print("csv파일을 csv로 만듭니다.")
        

        
if __name__=="__main__":
    # import argparse

    # parser = argparse.ArgumentParser()

    # parser.add_argument('--file_list', type=list, help='', default='')
    # parser.add_argument('--csv_name', type=str, help='', default='')

    # args = parser.parse_args()
    
    # tmp = Tocsv(args.file_list, args.csv_name)
    file_list = ""
    csv_name = ""
    tmp = Tocsv(file_list, csv_name)
    tmp.tocsv()


