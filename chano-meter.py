# import statements should generally be the very first line in a module
import re

# select a keyword (user input)
print("Welcome to the Chano-meter!")
keyword = input("Which word would you like to search for? ")

# while the keyword isn't a single word
while len(keyword.split()) > 1:
	keyword = input("Please submit a single word! ")

# create a dictionary of song names to file names
song_files = {"14,400 Minutes": "songs/14400minutes.txt",
"Missing You": "songs/missingyou.txt",
"Nostalgia": "songs/nostalgia.txt",
"Windows": "songs/windows.txt",
"Brain Cells": "songs/braincells.txt",
"Long Time": "songs/longtime.txt",
"22 Offs": "songs/22offs.txt",
"U Got Me Fucked Up": "songs/ugotmefuckedup.txt",
"Family": "songs/family.txt",
"Juke Juke": "songs/jukejuke.txt",
"Fuck You Tahm Bout": "songs/fuckyoutahmbout.txt",
"Long Time II": "songs/longtimeII.txt",
"Prom Night": "songs/promnight.txt",
"Hey Ma": "songs/heyma.txt",
"Good Ass Intro": "songs/goodassintro.txt",
"Pusha Man / Paranoia": "songs/pushamanparanoia.txt",
"Cocoa Butter Kisses": "songs/cocoabutterkisses.txt",
"Juice": "songs/juice.txt",
"Lost": "songs/lost.txt",
"Everybody's Something": "songs/everybodyssomething.txt",
"Interlude (That's Love)": "songs/thatslove.txt",
"Favorite Song": "songs/favoritesong.txt",
"NaNa": "songs/nana.txt",
"Smoke Again": "songs/smokeagain.txt",
"Acid Rain": "songs/acidrain.txt",
"Chain Smoker": "songs/chainsmoker.txt",
"Everything's Good (Good Ass Outro)": "songs/everythingsgood.txt",
"All We Got": "songs/allwegot.txt",
"No Problem": "songs/noproblem.txt",
"Summer Friends": "songs/summerfriends.txt",
"D.R.A.M. Sings Special": "songs/special.txt",
"Blessings": "songs/blessings.txt",
"Same Drugs": "songs/samedrugs.txt",
"Mixtape": "songs/mixtape.txt",
"Angels": "songs/angels.txt",
"Juke Jam": "songs/jukejam.txt",
"All Night": "songs/allnight.txt",
"How Great": "songs/howgreat.txt",
"Smoke Break": "songs/smokebreak.txt",
"Finish Line / Drown": "songs/finishlinedrown.txt",
"Blessings (Reprise)": "songs/blessingsreprise.txt",}

tenday_files = {"14,400 Minutes": "songs/14400minutes.txt",
"Missing You": "songs/missingyou.txt",
"Nostalgia": "songs/nostalgia.txt",
"Windows": "songs/windows.txt",
"Brain Cells": "songs/braincells.txt",
"Long Time": "songs/longtime.txt",
"22 Offs": "songs/22offs.txt",
"U Got Me Fucked Up": "songs/ugotmefuckedup.txt",
"Family": "songs/family.txt",
"Juke Juke": "songs/jukejuke.txt",
"Fuck You Tahm Bout": "songs/fuckyoutahmbout.txt",
"Long Time II": "songs/longtimeII.txt",
"Prom Night": "songs/promnight.txt",
"Hey Ma": "songs/heyma.txt",}

acidrap_files = { "Good Ass Intro": "songs/goodassintro.txt",
"Pusha Man / Paranoia": "songs/pushamanparanoia.txt",
"Cocoa Butter Kisses": "songs/cocoabutterkisses.txt",
"Juice": "songs/juice.txt",
"Lost": "songs/lost.txt",
"Everybody's Something": "songs/everybodyssomething.txt",
"Interlude (That's Love)": "songs/thatslove.txt",
"Favorite Song": "songs/favoritesong.txt",
"NaNa": "songs/nana.txt",
"Smoke Again": "songs/smokeagain.txt",
"Acid Rain": "songs/acidrain.txt",
"Chain Smoker": "songs/chainsmoker.txt",
"Everything's Good (Good Ass Outro)": "songs/everythingsgood.txt",}

coloringbook_files = {"All We Got": "songs/allwegot.txt",
"No Problem": "songs/noproblem.txt",
"Summer Friends": "songs/summerfriends.txt",
"D.R.A.M. Sings Special": "songs/special.txt",
"Blessings": "songs/blessings.txt",
"Same Drugs": "songs/samedrugs.txt",
"Mixtape": "songs/mixtape.txt",
"Angels": "songs/angels.txt",
"Juke Jam": "songs/jukejam.txt",
"All Night": "songs/allnight.txt",
"How Great": "songs/howgreat.txt",
"Smoke Break": "songs/smokebreak.txt",
"Finish Line / Drown": "songs/finishlinedrown.txt",
"Blessings (Reprise)": "songs/blessingsreprise.txt",}

# make the songs dictionary, using the filenames dictionary
songs = {}
for song_file in song_files:
	fv = open(song_files[song_file])
	songs[song_file] = "".join(fv.readlines()).lower()
	fv.close()

tenday = {}
for tenday_file in tenday_files:
	fv = open(tenday_files[tenday_file])
	tenday[tenday_file] = "".join(fv.readlines()).lower()
	fv.close()

acidrap = {}
for acidrap_file in acidrap_files:
	fv = open(acidrap_files[acidrap_file])
	acidrap[acidrap_file] = "".join(fv.readlines()).lower()
	fv.close()

coloringbook = {}
for coloringbook_file in coloringbook_files:
	fv = open(coloringbook_files[coloringbook_file])
	coloringbook[coloringbook_file] = "".join(fv.readlines()).lower()
	fv.close()

artist = "Chano"

# create a mixtape
mixtape_name1 = "10 Day"
mixtape1_lyrics = ""
for tenday_songs in tenday:
	mixtape1_lyrics += tenday[tenday_songs]

mixtape_name2 = "Acid Rap"
mixtape2_lyrics = ""
for acidrap_songs in acidrap:
	mixtape2_lyrics += acidrap[acidrap_songs]

mixtape_name3 = "Coloring Book"
mixtape3_lyrics = ""
for coloringbook_songs in coloringbook:
	mixtape3_lyrics += coloringbook[coloringbook_songs]

# count and print for mixtapes!
print("")
print("%s said the word %s..." % (artist, keyword))

tenday_word_count = re.sub("[^\w]", " ", mixtape1_lyrics).split().count(keyword.lower())
print("%d time%s on the mixtape %s!" % (tenday_word_count, "" if (tenday_word_count == 1) else "s", mixtape_name1))

acidrap_word_count = re.sub("[^\w]", " ", mixtape2_lyrics).split().count(keyword.lower())
print("%d time%s on the mixtape %s!" % (acidrap_word_count, "" if (acidrap_word_count == 1) else "s", mixtape_name2))

coloringbook_word_count = re.sub("[^\w]", " ", mixtape3_lyrics).split().count(keyword.lower())
print("%d time%s on the mixtape %s!" % (coloringbook_word_count, "" if (coloringbook_word_count == 1) else "s", mixtape_name3))

# count and print for each song
print("")
print("%s said the word %s..." % (artist, keyword))

for song in songs:
	word_count = re.sub("[^\w]", " ",  songs[song]).split().count(keyword.lower())
	if (word_count != 0):
		print("%d time%s in the song %s!" % (word_count, "" if (word_count == 1) else "s", song))
