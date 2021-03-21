#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import string
import random

import datetime as dt

#Get all characters letters
all_char = list(string.printable)

#Zip the alphabet and its corresponding number in the alphabet together in a dictionary
num_alpha = dict(zip(list(range(len(string.printable[:95]))),all_char))

#Scramble the entire string.printable list. Has digits, letters, and symbols. Removes \t,\n,\r,\x0b,\x0c
new_list = sorted( range(len(string.printable[:95])), key = lambda x: random.random() )

#Create the encrypted list that uses the scrambled numbers from new_list to create a random encryption
encrypted_list = [num_alpha[number] for number in new_list]

#Create the dictionary that encodes the raw message
encrypt_dict = dict(zip(list(num_alpha.values()),encrypted_list))

#Create the decrypter  
decrypt_dict = {v: k for k,v in encrypt_dict.items()}

#Read our message
raw_message = ''.join([line.rstrip() for line in open('text_to_read')])


#IMPORTANT NOTE
'''
Sometimes you'll run into issues where you copy and paste a passage from the internet and the formatting of an apostraphe
doesn't register as a valid character in string.printable. Annoying to deal with, that said, if you were really using this
to send encoded messages, you're probably not just copying things from the internet
'''


#Encode the message
encrypted_message=''.join([encrypt_dict[thing] for thing in raw_message])

#Decoded messages
decrypted_message = ''.join([decrypt_dict[thing] for thing in encrypted_message])

#Check if the raw message and our decoded message is the same
message_check = raw_message == decrypted_message
