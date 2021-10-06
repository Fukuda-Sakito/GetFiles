#! /bin/python

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from os.path import expanduser
import shutil
home = expanduser("~")

# ホームディレクトリに mypasswd.txt を配置し，内容を以下の形式にする．
# <アカウント>
# <アカウントのパスワード>
# <Chromedriver の path>
f = open(f"{home}/mypasswd.txt", 'r', encoding='UTF-8')
datalist = f.readlines()
f.close()

USER = datalist[0].strip()
PASS = datalist[1].strip()
driver_path = datalist[2].strip()

options = Options()  # Chromeを起動
download_dir = "~/infoss-auto/"
prefs = {"download.default_directory": f"{download_dir}"}  # ダウンロード先の Path を指定
options.add_experimental_option("prefs", prefs)  # ダウンロード先をオプションで指定
options.add_argument('--headless')  # ヘッドレスモード
# Chrome Driverを起動する
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
driver.implicitly_wait(100)  # 処理時に最長100秒待つ
driver.set_script_timeout(10)  # Javascript実行が終了するまで最大5秒間待つように指定
driver.delete_all_cookies()  # 全てのクッキーを削除


def main():
    logIn()
    getFiles("file1")
    getFiles("file2")
    getFiles("file3")
    getFiles("file4")
    getFiles("file5")
    driver.quit()  # ブラウザを終了する


def logIn():
    url_login = "https://logInPath"  # ログインサイト path
    driver.get(url_login)  # ログインページを開く

    checkURL()

    element = driver.find_element_by_id("username")
    element.clear()
    element.send_keys(USER)
    element = driver.find_element_by_id("password")
    element.clear()
    element.send_keys(PASS)
    element = driver.find_element_by_name("_eventId_proceed")
    element.click()

    checkURL()

    element = driver.find_element_by_id("username")
    element.clear()
    element.send_keys(USER)
    element = driver.find_element_by_id("password")
    element.clear()
    element.send_keys(PASS)
    element = driver.find_element_by_id("LoginBtn")
    element.click()

    checkURL()
    # トップページに入れたはず


def selectYear():
    dropdown = driver.find_element_by_name('year')
    select = Select(dropdown)
    select.select_by_value('all')  # valueが"all"のoptionタグを選択状態にする
    cur_url = driver.current_url  # カレントページのURLを表示
    print(cur_url)


def checkURL():
    time.sleep(0.1)
    cur_url = driver.current_url  # カレントページのURLを表示
    print(cur_url)


def getFiles(kind):
    selectYear()

    # kindで指定されたバージョンのxpathを取得
    if kind == "file1":
        next_xpath = "Full X Path"
    elif kind == "file2":
        next_xpath = "Full X Path"
    elif kind == "file3":
        next_xpath = "Full X Path"
    elif kind == "file4":
        next_xpath = "Full X Path"
    elif kind == "file5":
        next_xpath = "Full X Path"

    element = driver.find_element_by_xpath(next_xpath)
    element.click()  # kindで指定したコースへ移動

    time.sleep(0.1)
    cur_url = driver.current_url
    print(kind + ": " + cur_url)  # カレントページのURLを表示

    element = driver.find_element_by_xpath("Full X Path")
    element.click()  # 目的地のボタンをクリック
    element = driver.find_element_by_xpath("Full X Path")
    element.click()  # 目的地のボタンをクリック

    time.sleep(1)
    element = driver.find_element_by_xpath("Full X Path")
    driver.switch_to.frame(iframe)  # 操作フレームの切り替え

    element = driver.find_element_by_xpath("Full X Path")
    element.click()  # 目的地のボタンをクリックして展開

    time.sleep(1)
    element = driver.find_element_by_xpath("Full X Path")
    element.click()  # 目的地にチェック
    time.sleep(1)

    if kind == "file5":
        # 期間指定
        dropdown = driver.find_element_by_xpath('Full X Path')
        select = Select(dropdown)
        select.select_by_value('2015')  # valueが"2015"のoptionタグを選択状態にする
        dropdown = driver.find_element_by_xpath('Full X Path')
        select = Select(dropdown)
        select.select_by_value('1')  # valueが"1"のoptionタグを選択状態にする
        dropdown = driver.find_element_by_xpath('Full X Path')
        select = Select(dropdown)
        select.select_by_value('1')  # valueが"1"のoptionタグを選択状態にする
        time.sleep(1)

    element = driver.find_element_by_xpath("Full X Path")
    element.click()  # 再読み込みをクリック
    time.sleep(1)

    # 以下，ダウンロードをする処理
    element = driver.find_element_by_xpath("/html/body/div/form/p[2]/a")
    element.click()  # 「この表をダウンロード」をクリック

    driver.switch_to.window(driver.window_handles[-1])  # 操作ウインドウの切り替え(最新のウインドウに切り替え)
    time.sleep(2)

    element = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/a[2]/span")
    element.click()  # 「result-utf8.txt」をクリック

    element = driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td/a")
    element.click()  # 閉じるをクリック

    driver.switch_to.window(driver.window_handles[0])  # 操作ウインドウを戻す
    driver.switch_to.frame(iframe)  # 操作フレームの切り替え

    element = driver.find_element_by_xpath("/html/body/div/form/h3/a")
    element.click()  # 展開した部分を戻すためボタンをクリック
    time.sleep(0.5)
    driver.switch_to.default_content()  # 操作フレームを戻す

    return_top()  # Webclassトップページに戻る
    moveFile(kind)


def return_top():
    element = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/button/span")
    element.click()  # xボタンをクリックして閉じる
    element = driver.find_element_by_xpath("/html/body/header/nav/div[1]/div/div/a[1]")
    element.click()  # 画面の左上のボタンをクリックしてトップページへ移動
    checkURL()


def moveFile(kind):
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

    shutil.move(f"{download_dir}result-utf8.txt", f"{home}/{file_name}")


if __name__ == '__main__':
    main()
