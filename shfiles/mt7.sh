      START=$( date +"%T.%N")
        echo "$START" >> ./shfiles/files/mt7.txt
        mongotop --port 27017 >> ./shfiles/files/mt7.txt


