#!/bin/bash
set +m

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color
print () {
    printf -- "$1\n"
}

/usr/games/cowsay "Welcome to [[No Touch No See]]"
print "Here are the files we have in the directory"
print "-------------------------------------------"
ls
print "-------------------------------------------"
print ""
print "All the best!"
