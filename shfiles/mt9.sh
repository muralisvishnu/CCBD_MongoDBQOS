      START=$( date +"%T.%N")
        echo "$START" >> ./shfiles/files/mt9.txt
        mongotop --port 27019 >> ./shfiles/files/mt9.txt
