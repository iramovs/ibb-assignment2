#!/bin/bash

arr1=( 1.01 1.03 1.05 1.08 1.1 1.2 1.3 )
arr2=( 2 3 4 5 6 7 8 )

models=( 0 1 2 )

for m in "${models[@]}"
do
	echo "model $m"

	for i in "${arr1[@]}"
	do
		python3 detector_ear_haar_pretrained.py "$i" 5 "$m"
	done

	echo

	for i in "${arr2[@]}"
	do
		python3 detector_ear_haar_pretrained.py 1.05 "$i" "$m"
	done

	echo

done
