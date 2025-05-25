import os

#Defining function function file
def file():
    file = input("File Name:")
#Error checking
    while not os.path.exists(file):
        print("Incorrect File")
        file = input("File Name:")
    return file

#Function for reading file
def readfile(file):
    try:
        input_list = []
        user_file = open(file, "r")

        for word in user_file:
            word = word.strip("\n")
            input_list.append(word)
        user_file.close()
        return input_list
    # If an error occurs the program will end
    except ValueError:
        return ["An Error occurred"]

#Wordle aid tool function
def wordle_tool(list_of_words):
    user_choice = int(input("Which option do you want?(1,2,3,4)"))
    newuser_file = input("What would you like the name of your new file to be?")
    newfile = open(newuser_file, "w")
#Addition to function inorder to find all words that include the user chossen letter
    if user_choice == 1:
        letter_list = []
        user_letter = input("What letter did You input?")
        for word in list_of_words:
            temp = list(word)
            for letter in temp:
                if letter == user_letter:
                    letter_list.append(word)
        for word in letter_list:
            print(word, file=newfile)
        newfile.close()
        print(letter_list)
        return letter_list
#Addition to function which creates a separate file which holds all 5 letter words that have the user chossen letter in the chossen position
    elif user_choice == 2:
        letter_list = []
        user_letter = input("What letter did You input?")
        letter_position = int(input("Wheres the letter located?(1,2,3,4,5)"))
        for word in list_of_words:
            temp = list(word)
            if temp[letter_position-1] == user_letter:
                letter_list.append(word)
        for word in letter_list:
            print(word, file=newfile)
        newfile.close()
        print(letter_list)
        return letter_list
#addition to function which creates a separate file which outputs all the 5 letter words that contain the selected number of vowels
    elif user_choice == 3:
        letter_list = []
        number_vowels = int(input("How many Vowels are in the word(1,2,3,4,5)"))
        for word in list_of_words:
            temp = list(word)
            count = 0
            for letter in temp:
                if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
                    count +=1
                    if count == number_vowels:
                        letter_list.append(word)
        for word in letter_list:
            print(word, file=newfile)
        newfile.close()
        print(letter_list)
        return letter_list
#Addition to function that creates a seperate file which outputs 5 letter words that contain the chossen letter in the third position of the word
    elif user_choice == 4:
        letter_list = []
        middle_letter = input("Whats the middle letter?")
        for word in list_of_words:
            temp = list(word)
            if temp[2] == middle_letter:
                letter_list.append(word)
        for word in letter_list:
            print(word, file=newfile)
        newfile.close()
        print(letter_list)
        return letter_list




#Main function
def main():
    wordle_tool(readfile(file()))


main()
