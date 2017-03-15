# import statements should generally be the very first line in a module
import re

# select a keyword (user input)
keyword = input("What keyword would you like to search for? ")

# while the keyword isn't a single word
while len(keyword.split()) > 1:
	keyword = input("Please input a single word to search for! ")

# create a dictionary of song names to file names
song_files = {"14,400 Minutes": "14400minutes.txt",
"Missing You": "missingyou.txt",
"Nostalgia": "nostalgia.txt",
"Windows": "windows.txt",
"Brain Cells": "braincells.txt",
"Long Time": "longtime.txt",
"22 Offs": "22offs.txt",
"U Got Me Fucked Up": "ugotmefuckedup.txt",
"Family": "family.txt",
"Juke Juke": "jukejuke.txt",
"Fuck You Tahm Bout": "fuckyoutahmbout.txt",
"Long Time II": "longtimeII.txt",
"Prom Night": "promnight.txt",
"Hey Ma": "heyma.txt"}

# make the songs dictionary, using the filenames dictionary
songs = {}
for song_file in song_files:
	fv = open(song_files[song_file])
	songs[song_file] = "".join(fv.readlines()).lower()
	fv.close()

artist = "Chano"

# count and print keyword count for each song
for song in songs:
	word_count = re.sub("[^\w]", " ",  songs[song]).split().count(keyword.lower())
	if (word_count != 0):
		print("%s said the word %s %d time%s in the song %s!" % (artist, keyword, word_count, "" if (word_count == 1) else "s", song))

# create a mixtape
mixtape_name = "10Day"
mixtape_lyrics = ""
for song in songs:
	mixtape_lyrics += songs[song]

# count and print for mixtape!
word_count = re.sub("[^\w]", " ", mixtape_lyrics).split().count(keyword.lower())
print("%s said the word %s %d time%s on the mixtape %s!" % (artist, keyword , word_count, "" if (word_count == 1) else "s", mixtape_name))