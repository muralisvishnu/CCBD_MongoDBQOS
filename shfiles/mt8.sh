      START=$( date +"%T.%N")
        echo "$START" >> ./shfiles/files/mt8.txt
        mongotop --port 27018 >> ./shfiles/files/mt8.txt
