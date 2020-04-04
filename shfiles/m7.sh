       START=$( date +"%T.%N")
        echo "$START" >> ./shfiles/files/m7.txt
        mongostat --port 27017 >> ./shfiles/files/m7.txt
