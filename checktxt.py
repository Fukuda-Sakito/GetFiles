#! /bin/python

import sys
import os
from os.path import expanduser
import datetime
home = expanduser("~")

f = open(f"{home}/mypasswd.txt", 'r', encoding='UTF-8')
datalist = f.readlines()
f.close()
USER = datalist[0].strip()

judge = True  # OKならTrue、NGならFalse
file5_year = int(datetime.date.today().year) - 6 # 現在の年を整数型で取得し、-6年する
file5_range = str(file5_year) + "-1-1" # file5 の実施範囲のスタートの年月日を文字列として格納
# print(file5_range)


def main():
    check_file("file1")
    check_file("file2")
    check_file("file4")
    check_file("file4")
    check_file("file5")

    # 一通り見て何かしら問題があったら終了する
    if not judge:
        sys.exit(1)


def check_file(kind):
    if kind == "file1":
        file_name = "result-utf8.txt"
    elif kind == "file2":
        file_name = "result-utf8 (1).txt"
    elif kind == "file3":
        file_name = "result-utf8 (2).txt"
    elif kind == "file4":
        file_name = "result-utf8 (3).txt"
    elif kind == "file5":
        file_name = "result-utf8 (4).txt"
    if os.path.isfile(f"{home}/{file_name}"):
        check_string(kind)
    else:
        print(f"{file_name} がありません")
        judge = False


def check_string(kind):
    if kind == "file1":
        file_name = "result-utf8.txt"
        text = "確認"
        title = text
    elif kind == "file2":
        file_name = "result-utf8 (1).txt"
        text = "確認"
        title = text
    elif kind == "file3":
        file_name = "result-utf8 (2).txt"
        text = "確認"
        title = text
    elif kind == "file4":
        file_name = "result-utf8 (3).txt"
        text = "確認"
        title = text
    elif kind == "file5":
        file_name = "result-utf8 (4).txt"
        text = "確認"
        title = text

    f = open(f"{home}/{file_name}", 'r', encoding='UTF-8')
    file_data = f.readlines()
    data_strip = [line.strip() for line in file_data]
    f.close()  # 確認するファイルの内容を取得した

    # 文章を確認する
    l_admin = [line for line in data_strip if USER in line]
    l_type = [line for line in data_strip if text in line]

    # file5は実施期間も含めて確認
    if kind == "file5":
        l_date = [line for line in data_strip if file5_range in line]
        check_list = str(l_admin + l_date + l_type)
        if USER in check_list and text in check_list and file5_range in check_list:
            print(f"{title} を確認しました．")
        else:
            print(f"取得した{title} に問題があります．")
            judge = False

    # file3の処理
    elif kind == "file3":
        l_file1 = [line for line in data_strip if "確認" in line]
        l_file2 = [line for line in data_strip if "確認" in line]
        check_list = str(l_admin + l_type + l_file1 + l_file2)

        # 確認事項が含まれ、file3でもfile5でもなければ通常版
        if USER in check_list and text in check_list and "確認" not in check_list and "確認" not in check_list:
            print(f"{title} を確認しました．")
        else:
            print(f"取得した{title} に問題があります．")
            judge = False

    # file1, file2, file4, の処理
    else:
        check_list = str(l_admin + l_type)
        if USER in check_list and text in check_list:
            print(f"{title} を確認しました．")
        else:
            print(f"取得した{title} に問題があります．")
            judge = False


if __name__ == '__main__':
    main()
