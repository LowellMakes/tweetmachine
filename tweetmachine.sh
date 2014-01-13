#!/bin/bash

log="twitterlog.txt"
ignore="twitterignorelist.txt"
gennumber=$(seq 1000 9999 | sort -R | head -1)
ttytter="/home/leftyfb/ttytter"

if [ -n "$1" ] ;then
	number=$1
else
	number=$gennumber
fi
#echo "gennumber = $gennumber"
echo "number = $number"

echo "setting COUNTER = 0"
COUNTER=0

gettweet(){
	pulltweet=$($ttytter -runcommand="/replies" |tail -n1)
	echo $($ttytter -runcommand="/replies")
	tweet=$pulltweet
	name=$(echo $tweet|awk -F '[<|>]' '{print $2}')
	tnumber=$(echo $tweet|grep -Eo '[0-9]{4}')
	alreadytweeted=$(grep ^$name$ $ignore|wc -l)
	sleep 30
}

while [ $COUNTER -lt "4" ]; do
		gettweet
		echo "tweet = $tweet"
		echo "name = $name"
		echo "number = $number"
		echo "tnumber = $tnumber"
		echo "alreadytweeted = $alreadytweeted"
		if [ -z "$tweet" ] ;then
			echo "Something is wrong"
			exit 1
		fi
		if [ "$number" = "$tnumber" ];then
			if [ $alreadytweeted = "1" ]; then
				$ttytter -runcommand="@$name Sorry, but you already got a prize."
				echo "tweeted back, $name already tweeted"
				exit 0
			elif [ $alreadytweeted = "0" ]; then
				echo "@$name tweeted the correct number $tnumber"
				$ttytter -runcommand="Congrats to @$name for his free tweetmachine prize!"
				echo "dispense toy"
				echo "$(date) $name" >> $log
				echo "$name" >> $ignore
				exit 0
			fi
		fi
		let COUNTER=COUNTER+1
		echo "COUNTER = $COUNTER"
done
