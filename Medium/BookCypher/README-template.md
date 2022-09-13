# SongLookup

* **Category:** Medium
* **Mode:** Online
* **Authors:**
  * Anish
  * Anmol 
* **Points:** TBD

## Specifications

* **Entry point:** `<clue>`
* **Reward:** TBD (Usually a clue to another question)

## Description

Players are given 3 different clues to 3 different songs (more specifically, 3 particular words in the song). Each song has its own different way of obtaining the word. Players are informed beforehand that the solution is in the format `part1-part2-part3`. For song 1 (part 1), an audio clip along with a picture of a clock with a specific time. For song 2 (part 2), Players will be given a scripture from the bible(TBD), which gives them a clue to the time stamp. Along with this they will get the location (SMV 102 or such) of the QR code which, when scanned, loads the song. For song 3 (part 3) a text file with encrypted lyrics along with thte timestamp which has already been encrypted once, is provided.

## Solution

1. For song 1, shazam the song loop, observe the clock for timestamp, navigate to song on youtube and input lyric corresponsing to that timestamp
2. For song 2, Look up scipture, find the timestamp given, also navigate to given location in question and scan QR code in said location, this will load a song. Using the timestamp, input the lyric as solution.
3. For song 3, Download file, decrypt lyrics, find song, decrypt timestamp, find word
4. Combine all the words and submit answer 

## Hints:

 - Hint for song 1 --> Shazam (Cost = TBD) 
 - Hint for song 2 --> Bible verse (Cost = TBD)
 - Hint for song 3 --> Decrypt twice (Cost = TBD)