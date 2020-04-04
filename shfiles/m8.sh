      START=$( date +"%T.%N")
        echo "$START" >> ./shfiles/files/m8.txt
        mongostat --port 27018 >> ./shfiles/files/m8.txt


