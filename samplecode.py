
""" data extraction regex source code by sabrina"""
import re


""" Get data from a text file """
with open('sampleinput.txt', 'r') as f:
    data = f.read()

""" Risky patterns to look for """
wrong_pattern = ['<script>', '</script>', 'javascript:', 'onload=', 'onclick=', 'onerror=', 'select *', 'insert into', 'delete from', 'update set', 'drop']

""" Regex patterns for phone numbers, email addresses, hashtags, and time formats """
phone_number_pattern = r'^[0-9]{10}$'
""" """
email_address_pattern = r'^[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
hash_tag_pattern = r'#\w+'
time_pattern = r'\b\d{1,2}:\d{2}(?:\s*(?:AM|PM))?\b'

def security(word):
    """ Check if a word contains any risky patterns and return false """
    word_lower = re.findall
    for pattern in wrong_pattern:
        if pattern in word_lower:
            return False
    return True



    



    
