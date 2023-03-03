#!/usr/bin/env bash

read var

# 5+50*3/20 + (19*2)/7
# 17.92857142857142857143

result=$(echo $var | bc -l)



# printf %.2f $(echo "scale=2;$result" | bc)
# echo $result
printf %.3f $(echo $var | bc -l)
