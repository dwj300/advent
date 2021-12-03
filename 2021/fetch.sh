#!/bin/bash

DAY="$1"
YEAR="2021"

if [ -z "$DAY" ]; then
    echo "usage: ./fetch.sh [day]"
    exit 1
fi
curl -sS "https://adventofcode.com/$YEAR/day/$DAY/input" -H "$AOC_COOKIE" -o "$DAY.txt"
