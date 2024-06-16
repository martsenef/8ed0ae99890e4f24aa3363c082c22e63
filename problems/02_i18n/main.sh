#!/bin/bash

export TEXTDOMAINDIR="./locales"
export TEXTDOMAIN="main"

printf "['"$"Hello!""', '"$"My name is %s""']\n" $"testuser"
