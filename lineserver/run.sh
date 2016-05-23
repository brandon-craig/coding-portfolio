#!/bin/bash

usage() {
	echo "Usage: $0 [file]"
	exit 1
}

is_file_exists() {
	local f="$1"
	[[ -f "$f"  ]] && return 0 || return 1
}

[[ $# -gt 1 || $# -eq 0 ]] && usage

if (is_file_exists "$1")
then
	node app $1
else
	echo "File not found"
fi