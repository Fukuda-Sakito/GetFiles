#!/bin/sh


if [ -f "$1/result-utf8.txt" -a -f "$1/result-utf8 (1).txt" -a -f "$1/result-utf8 (2).txt" -a -f "$1/result-utf8 (3).txt" -a -f "$1/result-utf8 (4).txt" ]; then
    mv "$1/result-utf8.txt" "$1/result-utf8-english.txt"
    mv "$1/result-utf8 (1).txt" "$1/result-utf8-furigana.txt"
    mv "$1/result-utf8 (2).txt" "$1/result-utf8-normal.txt"
    mv "$1/result-utf8 (3).txt" "$1/result-utf8-rapid.txt"
    mv "$1/result-utf8 (4).txt" "$1/result-utf8-pledge.txt"
        exit 0
else
        echo "file(s) does not exist."
        exit 1
fi
