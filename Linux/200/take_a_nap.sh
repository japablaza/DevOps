#!/bin/bash

if [ "$1" == "" ] 
    then TIME=10
    else TIME=$1
fi

echo -e "I am going to nap for $TIME seconds\n"

sleep $TIME

echo -e "I took a nap for about $TIME seconds\n"