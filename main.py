"""
Created on Sat May 15 22:25:56 2021

@author: 91963
"""

import speech_recognition as sr
import random


def recognize_speech_from_mic(recognizer, microphone):

    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response
'''
this is used to recognize the voice and give it as the input and the game 
will work accordingly to it . 1st it will ask the name of the player and then
the game will start as the game starts the player is supposed to guess the 
number according to the number of blanks given if they dont guess it
correctly the player has lost the game . if guessed correctly the number will 
be filled in the blank space , if all the number guessed correctly the 
player wins the game .

''' 
print('what is your name: ')

recognizer = sr.Recognizer()
microphone = sr.Microphone()
guess = recognize_speech_from_mic(recognizer, microphone)
a=guess.values()
name=list(a)
#print(name[2]) 
name=name[2]
print("Good Luck ! let's start the game :  ", name)

'''
these are the number to be guessed by the player

'''

numbers = ['1323', '25', '3', '46','5', '644', '2', '8124',
         '90','234','4','56','1910','10','22','2003']

# Function will choose one random
# number from this list of numbers
number = random.choice(numbers)
  
print("Guess the numbers ")
 
guesses = ''
 
# any number of turns can be used here
turns = 12
 
 
while turns > 0:
     
    # counts the number of times a user fails
    failed = 0
     
    # all characters from the input
    # number taking one at a time.
    for char in number:
         
        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char)
             
        else:
            print("_")
             
            # for every failure 1 will be
            # incremented in failure
            failed += 1
             
 
    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win")
         
        # this print the correct numbers
        print("The number is: ", number)
        break
     
    # if user has input the wrong number then
    # it will ask user to enter another number
    
    print("guess a number :")
    recognizer = sr.Recognizer() 
    microphone = sr.Microphone() 
    gues = recognize_speech_from_mic(recognizer, microphone) 
    b=gues.values() 
    guess=list(b)
    #print(guess[2]) 
    guess=guess[2]
    
    # every input numbers will be stored in guesses
    guesses += guess
    
     
  # check input with the number in list of numbers given above
    if guess not in number:
         
        turns -= 1
         
        # if the number doesn’t match the in list of numbers given above
        
        # then “Wrong” will be given as output
        print("Wrong")
         
        # this will print the numbers of
        # turns left for the user
        print("You have", + turns, 'more guesses')
         
         
        if turns == 0:
            print("You Loose")
