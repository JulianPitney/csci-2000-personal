#!/bin/bash
#Julian Pitney - 100489210





touch "temp1"
head -n -$2  $3 > "temp1" 
touch "temp2"
tail -n +$1 "temp1" > "temp2"    
rm "temp1"
cat "temp2"
rm "temp2"

# working



