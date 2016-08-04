#!/usr/bin/env python
import sys

def main():
	file_name = sys.argv[1]
	f = open(file_name)
	file = f.read()
	start_index = file.find('TAG')
	if start_index > 0 : get_captions(start_index, file)
	else: print('No such tag. result = ' + str(start_index))

def get_captions(index, s):
	print len(s) - index
	index += 3
	title_offset = index + 30
	artis_offset = title_offset + 30
	album_offset = artis_offset + 30
	year_offset = album_offset + 4

	title = s[index : title_offset]
	artist = s[title_offset : artis_offset]
	album = s[artis_offset : album_offset]
	year = s[album_offset : year_offset]

	print('Title is: ' + title)
	print('Artist is: ' + artist)
	print('Album is: ' + album)
	print('Year is: ' + year)

main()