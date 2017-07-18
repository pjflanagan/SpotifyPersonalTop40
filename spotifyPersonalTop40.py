#!usr/bin/env python

tracks_to_add = []
tracks_to_remove = []
	
def addCall():
	return 0
	
def removeCall():
	return 0
	
def get40Songs():
	tracks_to_add = items
	return 0
	
def get40Playlist():
	tracks_to_remove = items
	return 0

def reset():
	tracks_to_add = []
	tracks_to_remove = []
	return 0
	
def __main__():
	get40Songs()
	get40Playlist()
	for track in tracks_to_remove:
		if track in tracks_to_add:
			tracks_to_remove.remove(track)
			tracks_to_add.remove(track)
	addCall()
	removeCall()
	reset()