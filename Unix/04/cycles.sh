for h in {01..24}
do
	echo $h
done

c=10
while [ $c -ge 0 ] 
do 
	echo "Test"
	let "c = c - 1"
done

#!/bin/bash
for (( c=1; c<=5; c++ ))
do  
   echo "Попытка номер $c"
done
