import os, sys, random, re
from dictionary.words import DICTIONARY
from random import choice

VARIABLES_PATTERN = r'\$(\w+)\s*=\s*'
VARIABLE_VALUES_PATTERN = r'\$(\w+)\s*=\s*(.*)'
BRACKET_PATTERN = r'\[([^"\[\]]+)\](?=(?:(?:[^"]*"){2})*[^"]*$)'
IP_ADDRESS_PATTERN = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'

def check_extension(filename: str) -> None:
    if not os.path.splitext(filename)[-1].lower() == '.ps1':
        print('[!!!] Please make sure your powershell script has the .ps1 extension')
        sys.exit(0)

def check_file_exists(filename: str) -> None:
    if not os.path.isfile(filename):
        print('[!!!] File does not exist')
        sys.exit(0)

def check_file_has_content(filename: str) -> None:
    if os.path.getsize(filename) < 0:
        print('[!!!] Supplied filename seems to be empty')
        sys.exit(0)

def return_random_word() -> str:
    return random.choice(DICTIONARY)

def randomly_capatalise(match) -> str:
    match_one = match.group(1)
    if match_one[0] == "'":
        return f'[{match_one}]'
    random_caps = ''.join(choice((str.upper, str.lower))(char) for char in match_one)
    return f'[{random_caps}]'

def strings_l2r(match) -> str:
    variable_name = match.group(1)
    variable_value = match.group(2)
    print(f'Variable name: {variable_name}')
    print(f'Variable value: {variable_value}')
    if variable_value[0] != "'" or re.search(IP_ADDRESS_PATTERN, variable_value):
        return f'${variable_name} = {variable_value}'
    reversed_value = variable_value[::-1]
    new_value = "@("
    for index, char in enumerate(reversed_value):
        if index == 0 or index == (len(reversed_value) - 1):
            continue
        if index == (len(reversed_value) - 2):
            new_value = new_value + f'"{char}"'
            continue
        new_value = new_value + f'"{char}",'
    new_value = new_value + ")"
    return f'${variable_name} = {new_value};[array]::Reverse(${variable_name});'

def change_ip_to_hex(match) -> str:
    ip_address = match.group(0)
    print(f'Ip address found: {ip_address}')
    try:
        splitted_address = ip_address.split('.')
    except Exception as e:
        print(f'I errored here: {e}')
        sys.exit()
    hex_address = '{:02X}{:02X}{:02X}{:02X}'.format(*map(int, splitted_address))
    return f'0x{hex_address}'

def get_story() -> str:
    amount_of_words = random.randrange(2, 20)
    story = '# '
    for i in range(amount_of_words):
        story = story + f'{return_random_word()} '
    return f'{story}'


