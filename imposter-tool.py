import random
import matplotlib.pyplot as plt

# function to draw random words from text file and avoiding duplicates while doing so
def random_words(filepath, n):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            words = file.readlines()
            words=[word.strip() for word in words]
            random.shuffle(words)
            selected_words=set()
            result=[]
            for word in words:
                if len(result)==n: #if the number of desired lines is reached without duplicates loop stops
                    break
                if word not in selected_words: # adds lines if not already part of the list
                    selected_words.add(word)
                    result.append(word)
            return result
    except FileNotFoundError: # error in if text files are missing
        return print("File not found. Sorry.") 
    
# function to print a table with numbers in the first column and words in the second one
def print_table_words(words):
    if not words:
        return
    print("{:<10}{:<20}".format("Number","Word")) 
    for i, line in enumerate(words, start=1):
        print("{:<10}{:<20}".format(i,line))
        
# function to count lines in a text file
def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        return 0
# function to plot the total number of words in defined text files that contain words of different complexity
def plot_words():
    file_paths = ["easy_words.txt", "intermediate_words.txt", "hard_words.txt"]
    total_lines = [count_lines_in_file(file_path) for file_path in file_paths]
    plt.bar(file_paths, total_lines, color=['blue', 'green', 'red'])
    plt.title('Number of Words for each Difficulty Level')
    plt.xlabel('Difficulty')
    plt.ylabel('Number of words')
    plt.show()

print("Welcome to this word generator for the game 'Imposter'. \nWith this tool you can generate a list of random words for you to play the game. \nMake sure to also get a list ready with the same number of columns and just the word 'Imposter' to play the game. \nHave fun!")

# loop to let users choose a difficulty level
while True:
    difficulty=input("Please choose a difficulty level (easy/intermediate/hard):") #input for difficulty level
    if difficulty == "easy":
        filepath="easy_words.txt"
        break #end loop if this level was chosen. do the same in the following for the other difficulty levels
    if difficulty == "intermediate":
        filepath="intermediate_words.txt"
        break
    if difficulty == "hard":
        filepath="hard_words.txt"
        break
    else:
        print("Please try again and choose a valid difficulty level. Your options are 'easy', 'intermediate' and 'hard'") #if an invalid input is given this message will print

# loop to choose the number of words for the list. This loop also allows the user to plot the total number of words in each difficulty level.
while True:
    n=input("How many words do you want for your game? If you want to see how many words are available for each difficulty level please enter show.")
    if n=="show": # plot of total number of words. Input window will appear again afterwards.
        plot_words()
        continue
    else:
        try:
            maximum=count_lines_in_file(filepath)
            n=int(n)
            if n-1<=maximum: # makes sure that if the input number is higher than the number of lines available in the text file no list is generated
                extracted_words=random_words(filepath,n)
                print_table_words(extracted_words) 
                print("Have fun with your game!")
                break
            else:
                print("Your input was too high. Please try again!")
        except ValueError:
            print("Your input was neither a number nor the word 'show'. Please try again!")