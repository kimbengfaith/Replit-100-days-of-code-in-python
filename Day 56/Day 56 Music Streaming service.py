# Day 56 Music Streaming Service

import csv, os

artist_list = []
unique_artist = []

def unique():
  for artist in unique_artist:
    print(f"\n{artist}")

def print_artist():
  for artist in artist_list:
    if artist not in unique_artist:
      unique_artist.append(artist)

with open("100MostStreamedSongs.csv") as file:
  streams = csv.DictReader(file)
  for row in streams:
    try:
      name = row["Artist(s)"]
      artist_list.append(name)
      os.mkdir(name)
    except:
      pass
      
    file_name = os.path.join(f"{name}/",row["Song"])
    f = open(file_name, "w")
    f.write(str(row))
    f.close()

print_artist()
unique()

    
    