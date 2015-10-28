#!/bin/bash
#Julian Pitney - 100489210





touch "temp1"
head -n -$2  $3 > "temp1" 
touch "temp2"
tail -n +$1 "temp1" > "temp2"

rm "temp1"


# now just output contents of temp 2 to stdout but i don't know how with 5 mins left



