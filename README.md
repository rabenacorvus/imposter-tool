# Imposter Tool

This repository is for sharing a short python program that allows for creating random numbered lists of words, based on different difficulties, for the game "Imposter".

# The Game Imposter
In this game each player gets a list of numbered words. One player instead gets a numbered list of the same length but the word for each entry is "imposter". As a next step a number is chosen at random/by one of the players. For a defined number of rounds each player says a word associated with the word next to the chosen number. Based on what the other players say the imposter has to blend in by saying a word that won't make the other players suspicious.
After the rounds are done the players have to choose the person they think is the imposter. 

If they are wrong the imposter wins.

If they are right, the imposter still has the chance to win by identifying the correct word. If the guess is wrong, the other players win.

I would recommend at least 4 players for this game, but even more make this game more interesting.

# The Tool
This tool draws from three lists of words of different complexity. It then allows to choose how many words should be in the list. I would recommend around 100 words. The list can then be used to print out the list for playing the game. Make sure to include a list with the word "imposter" as well before the start of the game!

There are text files in this repository to run the program. BUT these are just example lists created with the help of ChatGPT, so not all words might be perfectly suitable for playing. Feel free to make your own lists for the game!

# Note
This tool was part of an assignment for a university course that defined the length of the program as well. There are some additonal features I'd like this tool to handle (in the future?) as well:
* creating the imposter list as well
* give the option for a more detailed explanation of the game
* option to export a print-ready file of the lists
* have the plotted bars be labeled "easy", "intermediate" and "hard" instead of the file name.
* if there are duplicates in the text files and there are less unique words than requested, the total number of words in the created list isn't equal to the number from the input. I'd probably like to have an error message for this case, even though of course the lists themselves should be full of unique words to start with...