set terminal pngcairo enhanced font 'Helvetica, 12' size 700,400

set grid
#set decimalsign ','
#set xrange [200:2050]
#set xtics 200,200,2000
#set ylabel 'Maksimalni čas [ms]'
#set ytics 0,2.5,30
#set key top center

set output 'm0mins.png'
set title 'MCS model, scaleFactor=1.05'
set xlabel 'minNeighbors'
set yrange [0:0.6]
plot 'm0mins.dat' using 1:2 w lp pt 7 title 'IoU',\
     'm0mins.dat' using 1:3 w lp pt 7 title 'Precision',\
     'm0mins.dat' using 1:4 w lp pt 7 title 'Recall'


set output 'm0scales.png'
set title 'MCS model, minNeighbors=5'
set xlabel 'scaleFactor'
set yrange [0:0.6]
plot 'm0scales.dat' using 1:2 w lp pt 7 title 'IoU',\
     'm0scales.dat' using 1:3 w lp pt 7 title 'Precision',\
     'm0scales.dat' using 1:4 w lp pt 7 title 'Recall'
     
set output 'm1mins.png'
set title '20\_set1 model, scaleFactor=1.05'
set xlabel 'minNeighbors'
set yrange [0:1]
plot 'm1mins.dat' using 1:2 w lp pt 7 title 'IoU',\
     'm1mins.dat' using 1:3 w lp pt 7 title 'Precision',\
     'm1mins.dat' using 1:4 w lp pt 7 title 'Recall'


set output 'm1scales.png'
set title '20\_set1 model, minNeighbors=5'
set xlabel 'scaleFactor'
set yrange [0:1]
plot 'm1scales.dat' using 1:2 w lp pt 7 title 'IoU',\
     'm1scales.dat' using 1:3 w lp pt 7 title 'Precision',\
     'm1scales.dat' using 1:4 w lp pt 7 title 'Recall'


set output 'm2mins.png'
set title '35\_set1 model, scaleFactor=1.05'
set xlabel 'minNeighbors'
set yrange [0:0.6]
plot 'm2mins.dat' using 1:2 w lp pt 7 title 'IoU',\
     'm2mins.dat' using 1:3 w lp pt 7 title 'Precision',\
     'm2mins.dat' using 1:4 w lp pt 7 title 'Recall'


set output 'm2scales.png'
set title '35\_set1 model, minNeighbors=5'
set xlabel 'scaleFactor'
set yrange [0:0.6]
plot 'm2scales.dat' using 1:2 w lp pt 7 title 'IoU',\
     'm2scales.dat' using 1:3 w lp pt 7 title 'Precision',\
     'm2scales.dat' using 1:4 w lp pt 7 title 'Recall'
     
