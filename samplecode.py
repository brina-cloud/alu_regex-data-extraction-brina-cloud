import re



""" Get data from a text file """
with open('sampleinput.txt', 'r') as file:
    data = file.read()

""" Risky patterns to look for """
wrong_pattern = ['<script>', '</script>', 'javascript:', 'onload=', 'onclick=', 'onerror=', 'select *', 'insert into', 'delete from', 'update set', 'drop']

""" remove risky patterns from a raw data """
def security(word):
    """ Check if a word contains any risky patterns and return false """
    for pattern in wrong_pattern:
        word = re.findall(pattern, word, re.IGNORECASE)
        return False
    return True


""" Regex patterns for phone numbers, email addresses, hashtags, and time formats """
""" finds a match for a 10-digit phone number """
phone_number_pattern = r'\b\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}\b'
phone_number_val = []
phone_number = re.findall(phone_number_pattern, data)
for number in phone_number:
    phone_number_val.append(number)


""" finds a match for a standard email address format with alphanumeric characters, dots, underscores, percent signs, plus signs, and hyphens before the "@" symbol, followed by a domain name and a top-level domain """
email_address_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
email_address_val = []
email_addresses = re.findall(email_address_pattern, data)
for email in email_addresses:
    email_address_val.append(email)



""" finds a match for hashtags starting with # followed by alphanumeric characters and underscores """
hash_tag_pattern = r'#\w+'
hash_tag_val = []
hash_tags = re.findall(hash_tag_pattern, data)
for tag in hash_tags:
    hash_tag_val.append(tag)


""" finds a match for time formats like HH:MM or HH:MM AM/PM """
time_pattern = r'\b\d{1,2}:\d{2}(?:\s*(?:AM|PM))?\b'
time_val = []
times = re.findall(time_pattern, data)
for time in times:
    time_val.append(time)


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


with open('sampleoutput.txt', 'w') as f:
    f.write("Phone Numbers:\n")
    for number in phone_number_val:
        f.write(number + "\n")
    f.write("\nEmail Addresses:\n")
    for email in email_address_val:
        f.write(hide_email(email) + "\n")
    f.write("\nHashtags:\n")
    for tag in hash_tag_val:
        f.write(tag + "\n")
    f.write("\nTimes:\n")
    for time in time_val:
        f.write(time + "\n")
print("Data extraction complete. Check sampleoutput.txt for results.")

""" End of the code """



    



    
