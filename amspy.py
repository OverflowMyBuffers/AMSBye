# Amsbye or amspye, both work. Accept this joke.
import re, itertools, random
from utils import (
    VARIABLES_PATTERN,
    VARIABLE_VALUES_PATTERN,
    BRACKET_PATTERN,
    IP_ADDRESS_PATTERN,
    return_random_word,
    randomly_capatalise,
    strings_l2r,
    change_ip_to_hex,
    get_story
)

class AMSIPye:
    def __init__(self, input: str, output: str):
        self.input = input
        with open(input, 'r') as file:
                self.input_stream = file.read()
        self.output = output

    def write_to_output_file(self):
        output_file = open(self.output, 'w')
        output_file.write(self.input_stream)
        output_file.close()
        print(f'File written to {self.output}')

    def change_variable_names(self) -> None:
        variables = re.findall(VARIABLES_PATTERN, self.input_stream)
        for var in variables:
            old_variable_name = f'${var}'
            new_variable_name = f'${return_random_word().capitalize()}{return_random_word().capitalize()}'
            self.input_stream = self.input_stream.replace(old_variable_name, new_variable_name)

    def capatalise_functions(self) -> None:
        self.input_stream = re.sub(BRACKET_PATTERN, randomly_capatalise, self.input_stream)

    def left2right(self) -> list[str]:
        return_variables = []
        variable_pairs = re.findall(VARIABLE_VALUES_PATTERN, self.input_stream)
        for var in variable_pairs:
            variable_name = var[0]
            variable_value = var[1]
            if variable_value[0] == "'":
                return_variables.append(variable_name)
        self.input_stream = re.sub(VARIABLE_VALUES_PATTERN, strings_l2r, self.input_stream)
        return return_variables

    def replace_variables_except_first_and_second_to_join(self, variable_name: str) -> None:
        c = itertools.count()
        cp = itertools.count(step=1)
        regex = r'\$' + re.escape(variable_name)
        self.input_stream = re.sub(regex, lambda x:x.group() if not next(c) or not next(cp) else f'(-join({x.group()}))', self.input_stream)

    def ip_to_hex(self) -> None:
        self.input_stream = re.sub(IP_ADDRESS_PATTERN, change_ip_to_hex, self.input_stream)

    def write_random_comments(self) -> None:
        temp = self.input_stream.split('\n')
        total_lines = self.input_stream.count('\n')
        if total_lines == 0:
            return
        amount_of_comments = random.randrange(1, 5)
        for i in range(amount_of_comments):
            insert_location = random.randrange(0, total_lines)
            temp = temp[:insert_location] + [get_story()] + temp[insert_location:]
        self.input_stream = '\n'.join(temp)

    def convert_to_oneliner(self) -> None:
        remove_eol = self.input_stream.replace(';', '\n')
        temp = remove_eol.split('\n')
        self.input_stream = ';'.join(temp).replace(";;", ';')


