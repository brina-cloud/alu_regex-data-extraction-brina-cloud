
""" data extraction regex source code by sabrina"""
import re


""" Get data from a text file """
with open('sampleinput.txt', 'r') as f:
    data = f.read()

""" Risky patterns to look for """
wrong_pattern = ['<script>', '</script>', 'javascript:', 'onload=', 'onclick=', 'onerror=', 'select *', 'insert into', 'delete from', 'update set', 'drop']

phone_number_pattern = r'
email_address_pattern = r'
hash_tag_pattern = 
time_pattern = 




