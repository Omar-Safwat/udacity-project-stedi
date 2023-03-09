#!/bin/bash
# This script reformats json files into a format openX.SerDe expects
# Every json record is on one line in the output of the script.
dir=$(echo "$1" | sed 's#/$##')
for file in "$dir"/*.json; do
	# rename to temp file
	mv "$file" "$file.TEMP" 
	jq -c 'try . catch empty' "$file.TEMP" > "$file" \
	&& rm "$file.TEMP" \
	&& echo Done:"$file"
done	
