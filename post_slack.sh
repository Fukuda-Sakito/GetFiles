#! /bin/bash

# 実行者のユーザートークンを読み込む
# ~/mypasswd の4行目に"トークン"の形式で記載しておく
TOKEN=`cat ~/mypasswd.txt | head -4 | tail -1`

# 投稿先のチャンネル 現在は事務室になっている
TARGET="Channel ID"

# 投稿文
TEXT="<@test>先生 本日の反映が完了いたしました．ご確認お願いいたします．"

curl https://slack.com/api/chat.postMessage \
    -X POST \
    -H "Authorization: Bearer $TOKEN" \
    -d "channel=$TARGET" \
    -d "text=$TEXT" \
    -d "as_user=true"
