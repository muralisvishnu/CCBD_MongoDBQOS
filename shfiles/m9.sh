      START=$( date +"%T.%N")
        echo "$START" >> ./shfiles/files/m9.txt
        mongostat --port 27019 >> ./shfiles/files/m9.txt


