Fourier

●	Category: Hard
●	Mode: Online
●	Authors:
	○	Saharsh
	○	Hari
	○	Vidit
●	Points: TBD

Specifications
●	Entry point: The user will be given a musical piece
●	Requirement: 
●	Reward: TBD (Usually a clue to another question)

Description

The user will be given a musical piece, and will be told that there's a 3s error, every 15s. They'll have to cut out a 1s part out of every 3s error and create a concatenated audio file from them (1sec error, 1sec gap), and the order of the edited parts does matter. The errors will be matched with the elements of a dictionary in the backend (error - key, frequency - value). The elements in the dictionary will be 3s long (Do majority matching or something similar for convenience). The music piece will have 20 errors, and only one combination of 15 errors out of the 20 errors, is the correct answer. We can provide them with a script to form all the possible combinations and try them all out. For every combination the user submits, they will get a fourier series, which they'll have to visualize using a fourier series visualizer.

Solution

Hints:
●	Hint 1 (Cost = TBD)
●	Hint 2 (Cost = TBD)


Example

Given file: -----222----111-------444-----------------666------------333-------------999-------------
User submits: = = = = =
Our software: 
= = = = =
2 3 6 1 5

Stored {=: 1, =: 2, =: 3, =: 4, =: 5, =: 6, =: 7, =: 8, =: 9, =: 0}

Passed to the helper program: [2 3 6 1 5]

Helper program renders the image.

It renders the image following the order
