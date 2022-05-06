"""
Author: Chris Sigmund, csigmund@purdue.edu
Assignment: 12.1 - Solo Wof
Date: 11/24/2021

Description:
    This is a variation of the wheel of fotune game for a single player.
    This program emulates all of the rules and requirements of the regular
    wheel of fortune game including spinning the wheel, taking letter guesses
    from the user, etc...

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""
import random

def load_phrases():
    phrases = [] #list of phrases to be returned
    with open('phrases.txt') as fo:
        for line in fo:
            end = line.index("\n") #end index of the state
            phrases.append(line[:end])
    random.shuffle(phrases)
    return(phrases)

def spin_the_wheel():
    options = [500, 500, 500, 500, 550, 550, 600, 600, 600, 600, 650, 650, 650, 700, 700, 800, 800, 900, 2500, 'BANKRUPT', 'BANKRUPT']
    pick = random.choice(options)
    return(pick)

def print_game_board(phrase, round, remainingVowels, remainingConsonants, roundEarnings):
    roundEarnings = '${:,d}'.format(roundEarnings)
    print('\n:: Solo WoF :::::::::::::::::::::::::::::: Round {} of 4 ::'.format(round))
    print(':: {} ::'.format(phrase.center(52)))
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::') #60 wide
    print('::   {}   ::   {}   :: {} ::'.format(remainingVowels, remainingConsonants, roundEarnings.rjust(10)))
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print('\nMenu:')

def print_board():
    print('  1 - Spin the wheel.')
    print('  2 - Buy a vowel.')
    print('  3 - Solve the puzzle.')
    print('  4 - Quit the game.\n')

def getConsonant(remainder):
    vowels = 'AEIOU' #all vowels in alphabet
    while(True):
        answer = input('Pick a consonant: ') #input from user
        if(not(len(answer) > 1) and not(len(answer) == 0)):
            if(answer.isalpha()):
                answer = answer.upper() #answer to uppercase
                if answer not in vowels:
                    if answer in remainder:
                        break;
                    else:
                        print('The letter {} has already been used.'.format(answer))
                else:
                    print('Vowels must be purchased.')
            else:
                print('The character {} is not a letter.'.format(answer))
        else:
            print('Please enter exactly one character.')

    return(answer)

def move_choice():
    nums = '1234'
    while(True):
        answer = input('Enter the number of your choice: ')
        if answer in nums:
            break;
        else:
            print('"{}" is an invalid choice.'.format(answer))

    return(int(answer))

def check_consonant(guessLetter, phrase, pick): #checks for number of occurances of the given letter
    amount = 0 #number of letters in the phrase
    phrase = phrase.upper() #the given phrase converted to uppercase
    guessLetter = guessLetter.upper() #letter the user guessed to uppercase
    for letter in phrase:
        if(letter == guessLetter):
            amount += 1
    if(amount == 0):
        print("I'm sorry, there are no {}'s.".format(guessLetter))
        roundEarnings = 0
    elif(amount == 1):
        print("There is {} {}, which earns you ${:,d}.".format(amount, guessLetter, (amount * pick)))
        roundEarnings = amount * pick
    else:
        print("There are {} {}'s, which earns you ${:,d}.".format(amount, guessLetter, (amount * pick)))
        roundEarnings = amount * pick
    return(roundEarnings)

def check_vowel(guessLetter, phrase): #checks for number of occurances of the given letter
    amount = 0 #number of letters in the phrase
    phrase = phrase.upper() #the given phrase converted to uppercase
    guessLetter = guessLetter.upper() #letter the user guessed to uppercase
    for letter in phrase:
        if(letter == guessLetter):
            amount += 1
    if(amount == 0):
        print("I'm sorry, there are no {}'s.".format(guessLetter))
    elif(amount == 1):
        print("There is {} {}.".format(amount, guessLetter))
    else:
        print("There are {} {}'s.".format(amount, guessLetter))

def buy_vowels(remainingVowels):
    consonants = 'BCDFHGJKLMNPQRSTVWXYZ' #consonants in the alphabet
    while(True):
        answer = input('Pick a vowel: ') #answer from user
        if(not(len(answer) > 1) and not(len(answer) == 0)):
            if(answer.isalpha()):
                answer = answer.upper() #answer to uppercase
                if answer not in consonants:
                    if answer in remainingVowels:
                        break;
                    else:
                        print('The letter {} has already been purchased.'.format(answer))
                else:
                    print('Consonants cannot be purchased.')
            else:
                print('The character {} is not a letter.'.format(answer))
        else:
            print('Please enter exactly one character.')
    return(answer)

def update_letters(letter, letterList):
    for character in letterList:
        if(character == letter):
            i = letterList.index(character)
            a_string = letterList
            a_list = list(a_string)
            a_list[i] = ' '
            letterList = ''.join(a_list)
    return(letterList)

def createBlankPhrase(phrase):
    for character in phrase:
        if(character.isalpha()):
            i = phrase.index(character)
            a_string = phrase
            a_list = list(a_string)
            a_list[i] = '_'
            phrase = ''.join(a_list)
    return(phrase)

def updateBlankPhrase(phrase, blankPhrase, letter):
    letter = letter.upper()
    phrase = phrase.upper()
    for character in phrase:
        if(character == letter):
            i = phrase.index(character)
            a_string = phrase
            a_list = list(a_string)
            a_list[i] = " "
            phrase = ''.join(a_list)
            a_string = blankPhrase
            a_list = list(a_string)
            a_list[i] = letter
            blankPhrase = ''.join(a_list)
    return(blankPhrase)

def solve_puzzle(currentPhrase, phrase_guess_progress):
    print('Enter your solution.')
    print('  Clues: {}'.format(phrase_guess_progress))
    guess = input('  Guess: ')
    guess = guess.upper()
    if(guess == currentPhrase):
        return 1
    return 0


def main():
    phrases = load_phrases() #list with all phrases in a random order
    totalEarnings = 0 #total earnings the user has earned
    roundEarnings = 0 #earnings from the current round
    consonants = 'BCDFGHJKLMNPQRSTVWXYZ' #consonants in the alphabet
    vowels = 'AEIOU' #vowels in the alphabet
    round = 0 #round number
    cycle = 0 #number of attempts on current phrase
    roundOver = False
    gameOver = False
    letter = '' #letter that was chosen
    print('Welcome to Solo Wheel of Fortune!')
    while(not(gameOver) and round < 5):
        round += 1
        while(not(roundOver)):
            currentPhrase = phrases[round].upper()
            if(not(cycle)):
                remainingConsonants = consonants
                remainingVowels = vowels
                phrase_guess_progress = createBlankPhrase(currentPhrase)
            print_game_board(phrase_guess_progress, round, remainingVowels, remainingConsonants, roundEarnings)
            while(True):
                print_board()
                move = move_choice()
                if(move == 1 or move == 2 or move == 3 or move == 4):
                    break
                print('"{}" is an invalid choice.'.format(move))

            if(move == 1): #spin the wheel
                pick = spin_the_wheel()
                if(isinstance(pick, int)):
                    print('The wheel landed on ${:,d}.'.format(pick))
                    letter = getConsonant(remainingConsonants).upper()
                    roundEarnings += check_consonant(letter, currentPhrase, pick)
                    phrase_guess_progress = updateBlankPhrase(currentPhrase, phrase_guess_progress, letter)
                else:
                    print('The wheel landed on BANKRUPT.')
                    print('You lost ${:,d}!'.format(roundEarnings))
                    roundEarnings = 0

                remainingConsonants = update_letters(letter, remainingConsonants)

            elif(move == 2): #buy a vowel
                letter = buy_vowels(remainingVowels).upper()
                temp = check_vowel(letter, currentPhrase)
                phrase_guess_progress = updateBlankPhrase(currentPhrase, phrase_guess_progress, letter)
                roundEarnings -= 275
                remainingVowels = update_letters(letter, remainingVowels)
            elif(move == 3): #solve the puzzle
                print('Solve the puzzle')
                win = solve_puzzle(currentPhrase, phrase_guess_progress)
                if(win == 1):
                    print('Ladies and gentlemen, we have a winner!')
                    print('\n\nYou earned ${:,d} this round.'.format(roundEarnings))
                    totalEarnings += roundEarnings
                else:
                    print("I'm sorry. The correct solution was:")
                    print('{}'.format(currentPhrase.upper()))
                    print('\n\nYou earned $0 this round.\n')
                roundOver = True
            else:
                print('\nYou earned ${} this round.'.format(roundEarnings))
                print('\nThanks for playing!')
                totalEarnings += roundEarnings
                print('You earned a total of ${}.'.format(totalEarnings))
                gameOver = True;
                break

            cycle += 1


if __name__ == '__main__':
    main()
