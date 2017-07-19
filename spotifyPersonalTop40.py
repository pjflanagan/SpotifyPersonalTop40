#!usr/bin/env python

import credentials
import requests, json

tracks_to_add = []
tracks_to_remove = []

def authorize():
	url = "https://accounts.spotify.com/authorize"
	payload = {
		"client_id": credentials.CLIENT_ID,
		"response_type": "code",
		"redirect_uri": "http://localhost"
	}
	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'} #"Accept: application/json"
	r = requests.get(url, data=json.dumps(payload), headers=headers)
	print(r)
	return

def addCall():
	return 0

def removeCall():
	return 0

def get40Songs():
	url = "https://api.spotify.com/v1/me/tracks"
	payload = {}
	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'} #"Accept: application/json"
	r = requests.get(url, data=json.dumps(payload), headers=headers)
	#tracks_to_add = items
	return 0

def get40Playlist():
	#tracks_to_remove = items
	return 0

def reset():
	tracks_to_add = []
	tracks_to_remove = []
	return

authorize()
"""
get40Songs()
get40Playlist()
for track in tracks_to_remove:
	if track in tracks_to_add:
		tracks_to_remove.remove(track)
		tracks_to_add.remove(track)
addCall()
removeCall()
reset()
"""
