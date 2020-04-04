	START=$( date +"%T.%N")
	echo "$START" >> ./shfiles/files/dop.txt
	dstat >> ./shfiles/files/dop.txt
 
	
