while :
do
	Start=$( date +"%T.%N")
	repl8=$(mongo --port 27017 --eval "db.adminCommand( { replSetGetStatus : 1 } ).members[0].optimeDate - db.adminCommand( { replSetGetStatus : 1 } ).members[1].optimeDate")
	repl9=$(mongo --port 27017 --eval "db.adminCommand( { replSetGetStatus : 1 } ).members[0].optimeDate - db.adminCommand( { replSetGetStatus : 1 } ).members[2].optimeDate")
	rticket=$(mongo --port 27017 --eval "db.serverStatus().wiredTiger.concurrentTransactions.read.out")
	wticket=$(mongo --port 27017 --eval "db.serverStatus().wiredTiger.concurrentTransactions.write.out")
	ocursors=$(mongo --port 27017 --eval "db.serverStatus().metrics.cursor.open.total")
	aconn=$(mongo --port 27017 --eval "db.serverStatus().connections.available")
	pf=$(mongo --port 27017 --eval "db.serverStatus().extra_info.page_faults")
	memo=$(mongo --port 27017 --eval "db.serverStatus().mem.resident")
	dd=$(mongo --port 27017 --eval "db.serverStatus().wiredTiger.cache[\"bytes dirty in the cache cumulative\"]")
	bytescurrentused=$(mongo --port 27017 --eval "db.serverStatus().wiredTiger.cache[\"bytes currently in the cache\"]")
	readq=$(mongo --port 27017 --eval "db.serverStatus().globalLock.currentQueue.readers")
	writeq=$(mongo --port 27017 --eval "db.serverStatus().globalLock.currentQueue.writers")
	echo "$Start ${repl8:230} ${repl9:230} ${rticket:230} ${wticket:230} ${ocursors:241} ${aconn:230} ${pf:241} ${memo:230} ${dd:230} ${bytescurrentused:230} ${readq:230} ${writeq:230}" >> ./shfiles/files/check.txt
	sleep 0.11s
done
