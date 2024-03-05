#!/bin/bash

# Check if a path is provided
if [ $# -eq 0 ]; then
  	echo "Usage: $0 <path>"
 	exit 1
fi

if [[ ${1:0:1} != / ]]; then 
	echo "$1: Must be absoute path"
	exit 1
fi

# Get the provided path

sudo docker run -v $1:/mydev -p 80:80 amitsinghbal27/fastapi-webserver-v2
