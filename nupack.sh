#!/bin/bash
# run in adscodex directory
> dna.out
go run encode/main.go -tbl tbl -printfmt 1 -rndseed 40 $HOME/32kfilerand >> dna.out
mv dna.out $HOME/mfes/ads.in

mfes -material dna -multi $HOME/mfes/ads
# input file $HOME/mfes/ads.in, output file $HOME/mfes/ads.mfes

#########

cp dna.out $HOME/mfes/ads.in 

cat $HOME/mfes/ads.in | cut -b 1-145

echo -e "$(wc $HOME/mfes/ads.in)\n$(cat $HOME/mfes/ads.in)" > $HOME/mfes/ads.in

mfe -material dna -multi $HOME/mfes/ads

######
# for testing mfes  #programming-help

mkdir build && cd build
cmake ../
make
sudo make install

echo "4" >> $HOME/mfes.in 
echo "AAAAA" >> $HOME/mfes.in
echo "CCCCC" >> $HOME/mfes.in
echo "GGGGG" >> $HOME/mfes.in
echo "TTTTT" >> $HOME/mfes.in

mfes -material dna -multi $HOME/ads

####
# debugging nupack/mfes 
cd build
gdb --args bin/mfes -material dna -multi $HOME/mfes/mfes_4_v2