#!/bin/bash

Files/GetFiles/get_files.py
Files/GetFiles/checktxt.py

# 日付の取得
today=`date +%s`
day=`date +%Y%m%d%H%M`
AprilFirst=`date --date "\`date +%Y\`/04/01 00:00:00" +%s`
EndOfJune=`date --date "\`date +%Y\`/06/30 23:59:59" +%s`

# ファイルをフォルダに纏める
mkdir ~/Files-$day
mv ~/result-utf8* ~/Files-$day/
mv ~/Files-$day /home/cc/docs/Files/

# 作業ディレクトリへ移動
cd /home/cc/docs/Files
# 最新の作業ディレクトリを latest に取得
latest=`ls -tl |grep Files- |head -n 1 |cut -c 45- |cut -f 2 -d "-"`

# 以下，反映作業 まずはリネームする
Files/GetFiles/rename.sh Files-$latest
# 順番に実行ファイルを進めていく
# ここに反映作業に用いるスクリプトが入る．無くてもよい．

# エクセルへ記述するための実行ファイル
~/GetFiles/test.pl $latest

# エラー処理時，処理を止めて終了する
set -eu -o pipefail
function catch {
    echo "エラーが発生しました．"
}
function finally {
    echo "終了しました．"
}
trap catch ERR
trap finally EXIT

# 実行期間の切り分け
if [ $today -ge $AprilFirst ] && [ $today -le $EndOfJune ];then
    echo "期間中 4/1~6/30"
    # ここにも実行用スクリプトが入る
else
    echo "期間外 7/1~3/31"
    # ここにも実行用スクリプトが入る
fi

# 終了したら Slackで報告
~/GetFiles/post_slack.sh > /dev/null
