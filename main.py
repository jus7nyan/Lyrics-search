import lyricsgenius
import time
from os import system, path

token = "XHUCKXOEPYzU8jy0kopz6e5NdhNNnpoTxgOzlq5vSMhvIFjXB72W-Kc_JnKzJmZF"

genius = lyricsgenius.Genius(token)

get = input("Введите поисковый запрос: ")
print("\n\n")

def m_search(text):
	a = genius.search(text)

	artist = a["hits"][0]["result"]["artist_names"]
	title = a["hits"][0]["result"]["title"]

	song = genius.search_song(title,artist)

	lyrics = song.lyrics

	return [lyrics, artist, title]

song = m_search(get)
lyrics = song[0].replace("Embed","").replace("You might also like","")
artist = song[1]
title = song[2]

name = "'/tmp/"+artist+"_"+title+".txt'".replace(" ","_")


command = "nano -vxwmy " +name

system("clear")

if path.isfile(name):
	system(command)

else:
	file = open(name.replace("'",""),"w+")
	file.write(lyrics)
	file.close()
	system(command)

