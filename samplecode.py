
""" data extraction regex source code by sabrina"""
import re


""" Get data from a text file """
with open('sampleinput.txt', 'r') as f:
    data = f.read()

""" Risky patterns to look for """
wrong_pattern = ['<script>', '</script>', 'javascript:', 'onload=', 'onclick=', 'onerror=', 'select *', 'insert into', 'delete from', 'update set', 'drop']


phone_number_pattern = 
email_address_pattern = 
hash_tag_pattern = 
time_pattern = 

def security(word):
    """ Check if a word contains any risky patterns and return false """
    word_lower = word.lower()
    for pattern in wrong_pattern:
        if pattern in word_lower:
            return False
    return True



    



    
