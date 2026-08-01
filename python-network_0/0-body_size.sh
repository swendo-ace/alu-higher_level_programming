#!/bin/bash
# Takes a URL, sends a request, displays the response body size in bytes
curl -s "$1" | wc -c
