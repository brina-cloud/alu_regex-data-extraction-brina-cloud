import re
import json





""" Get data from a text file """
with open('sampleinput.txt', 'r') as file:
    data = file.read()

""" Risky patterns to look for """
wrong_pattern = ['<script>', '</script>', 'javascript:', 'onload=', 'onclick=', 'onerror=', 'select *', 'insert into', 'delete from', 'update set', 'drop']

""" remove risky patterns from a raw data """
def security(word):
    """ Check if a word contains any risky patterns and return false """
    for pattern in wrong_pattern:
        """ Check for each risky pattern """
        if re.search(pattern, word, re.IGNORECASE):
            return False
    return True


""" Regex patterns for phone numbers, email addresses, hashtags, and time formats """
""" finds a match for various phone number formats including optional parentheses, spaces, dashes, or dots """
phone_number_pattern = r'(?:\+\d{1,3}[-.\s]?)?(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}\b'
""" list to store extracted phone numbers """
phone_number_element = []
""" find all phone numbers in the data """
phone_number = re.findall(phone_number_pattern, data)
for number in phone_number:
    phone_number_element.append(number)


""" finds a match for a standard email address format with alphanumeric characters, dots, underscores, percent signs, plus signs, and hyphens before the "@" symbol, followed by a domain name and a top-level domain """
email_address_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
''' list to store extracted email addresses '''
email_address_element = []
""" find all email addresses in the data """
email_addresses = re.findall(email_address_pattern, data)
for email in email_addresses:
    email_address_element.append(email)



""" find s a match for hashtags starting with # followed by alphanumeric characters and underscores """
hash_tag_pattern = r'#\w+'
""" list to store extracted hashtags """
hash_tag_element = []
""" find all hashtags in the data """
hash_tags = re.findall(hash_tag_pattern, data)
for tag in hash_tags:
        hash_tag_element.append(tag)

""" finds a match for time formats like HH:MM or HH:MM AM/PM """
time_pattern = r'\b\d{1,2}:\d{2}(?:\s*(?:AM|PM))?\b'
""" list to store extracted time formats """
time_element = []
""" find all time formats in the data """
times = re.findall(time_pattern, data)
for time in times:
    time_element.append(time)


"""  function to write the extracted data to a new text file with some parts hidden for privacy """
def hide_email(email):
    """ hide some parts of the email for privacy """
    parts = email.split('@')
    local = parts[0]
    domain = parts[1]
    if len(local) <= 2:
        hidden_local = local[0] + '*' * (len(local) - 1)
    elif len(parts) != 2:
        return email
    else:
        hidden_local = local[0] + '*' * (len(local) - 2) + local[-1]
    return hidden_local + '@' + domain




""" this part writes the extracted and processed data to a new json file """
output_data ={
        "phone_numbers": phone_number_element,
        "email_addresses": [hide_email(email) for email in email_address_element],
        "hashtags": hash_tag_element,
        "times": time_element
    }
print(output_data)


""" convert the output data to a json string and write it to a file """
json_output = json.dumps(output_data, indent=4)
with open('sampleoutput.json', 'w') as json_file:
    json_file.write(json_output)
    print("Data extraction complete. Check sampleoutput.json for results.")







""" End of the code """



    



    
