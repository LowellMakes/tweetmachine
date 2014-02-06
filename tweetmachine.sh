#!/bin/bash

maindir=/home/pi/tweetmachine
log="$maindir/twitterlog.txt"
ignore="$maindir/twitterignorelist.txt"
gennumber=$(seq 1000 9999 | sort -R | head -1)
ttytter="/home/pi/ttytter"

if [ -n "$1" ] ;then
	number=$1
else
	number=$gennumber
fi
echo "number = $number"

echo "setting COUNTER = 0"
COUNTER=0

gettweet(){
	pulltweet=$($ttytter -runcommand="/replies" |tail -n1)
	tweet=$pulltweet
	name=$(echo $tweet|awk -F '[<|>]' '{print $2}')
	tnumber=$(echo $tweet|grep -Eo '[0-9]{4}')
	text=$(echo $tweet|grep -Eo 'lowellmakes'|wc -l)
	alreadytweeted=$(grep ^$name$ $ignore|wc -l)
	sleep 2
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
			#	$ttytter -runcommand="@$name Sorry, but you already got a prize."
				echo "tweeted back, $name already tweeted"
				exit 0
			elif [[ $alreadytweeted = "0" ]] && [[ $text = "1" ]]; then
				echo "@$name tweeted the correct number $tnumber"
				echo "dispense toy"
				python $maindir/pifacecode/piface.py -s b5
				echo "$(date) $name" >> $log
				echo "$name" >> $ignore
                sleep 10
				$ttytter -runcommand="Congrats to @$name for their free tweetmachine prize!"
				exit 0
			fi
		fi
		let COUNTER=COUNTER+1
		echo "COUNTER = $COUNTER"
done
