import pyperclip, re

#TODO: create regex object for phone number

phoneRegex = re.compile(r'''
                        (\d{3}|\(\d{3}\))?                # area code
                        (\s|\.|-)?                        # separator
                        (\d{3})                           # first three digit
                        (\s|\.|-)                         # separator
                        (\d{4})                           # last four digit
                        (\s*(ext|ext.|x)\s*(\d{2,5}))?    # extension
                        ''', re.VERBOSE)

##phone = phoneRegex.search('(123)-456-7890')
##print(phone.group(0))
##print(phone.group(1))
##print(phone.group(2))
##print(phone.group(3))
##print(phone.group(4))
##print(phone.group(5))
##print(phone.group(6))
##print(phone.group(7))
##print(phone.group(8))
##print(phone.group(9))
##print(phone.group(10))
##print(phone.group(11))


#TODO: create regex object for email

emailRegex = re.compile(r'''
                        [a-zA-Z0-9.+\-%_]+   # username
                        @                    # @ symbol
                        [a-zA-Z0-9.-]+       # domain name
                        (\.[a-zA-Z]{2,4})    # dot-something
                        ''', re.VERBOSE)

#TODO: Find matches in clipboard text

text = str(pyperclip.paste())

for phone in phoneRegex.findall(text):
    print(phone)

#TODO: Copy results to clipboard
