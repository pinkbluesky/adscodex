#!/bin/bash
# run in adscodex directory
> dna.out
go run encode/main.go -tbl tbl -rndseed 40 $HOME/filerand >> dna.out
mv dna.out $HOME/input/ads.in

mfes -material dna $HOME/mfes/ads
# output file $HOME/mfes/ads.mfes

#########

cat dna.out | cut -b 1-145
