#!/bin/sh

for g in graphs/*.dot
do
    echo "* $g"
    python3 run.py < $g
done
