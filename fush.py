###  # #  ###  # #
#    # #  #    # #
##   # #  ###  ###
#    # #    #  # #
#    ###  ###  # #

def execute(code):
    code = compile_code(code)
    print(f'FUSH code:\n{code[0]}')
    print(f'Python code:\n{code[1]}')
    print()
    exec(code[1])

def compile_code(code):
    code = code.split('\n')
    code_python = ''
    for line in code:

        stripped_line = line.strip()
        if not stripped_line:
            continue

        indent_level = len(line) - len(line.lstrip())

        if indent_level % 4 != 0:
            raise TabError('Invalid indent level. Expected multiple of 4.')

        indent_spaces = ' ' * (indent_level)

        code_python += indent_spaces

        parts = stripped_line.split(' ')
        # command = parts[0]

        # prints
        if parts[0] == 'output': # output Hello World
            print_result = ' '.join(parts[1:])
            code_python += f'print(\'{print_result}\')\n'
        elif parts[0] == 'outputf': # outputf <<x>>
            print_result = ' '.join(parts[1:])
            print_result = print_result.replace('<<', '{').replace('>>', '}')
            code_python += f'print(f\'{print_result}\')\n'

        # variables
        elif parts[0] == 'input': # input x
            code_python += f'{parts[1]} = input()\n'
        elif parts[0] == 'var': # check x == y
            if parts[1] == 'str' or parts[1] == 'string': # var str x "Hello World"
                code_python += f'{parts[2]} = str({parts[-1]})\n'
            elif parts[1] == 'dec' or parts[1] == 'decimal': # var dec x 10.5
                code_python += f'{parts[2]} = float({parts[-1]})\n'
            elif parts[1] == 'num' or parts[1] == 'number': # var num x 10
                code_python += f'{parts[2]} = int({parts[-1]})\n'
            elif parts[1] == 'stm' or parts[1] == 'statement': # var stm x True
                code_python += f'{parts[2]} = bool({parts[-1]})\n'
            else:
                code_python += f'{parts[1]} = {parts[-1]}\n'

        # conditions
        elif parts[0] == 'is': # is x == y
            if parts[2] == '=': parts[2] = '=='
            
            code_python += f'if {parts[1]} {parts[2]} {parts[3]}:\n'
        elif parts[0] == 'also': # also x == y
            if parts[2] == '=': parts[2] = '=='
            code_python += f'elif {parts[1]} {parts[2]} {parts[3]}:\n'

        elif parts[0] == 'otherwise': # otherwise
            code_python += f'else:\n'

        # cycles
        elif parts[0] == 'until':
            if len(parts) == 1:
                code_python += f'while True:\n'
            else:
                if parts[2] == '=': parts[2] = '=='
                code_python += f'while {parts[1]} {parts[2]} {parts[3]}:\n'
#                                  0    1    3       5 6
        elif parts[0] == 'loop': # loop i to 10 from 0 i+5
            if len(parts) == 7:
                code_python += f'for {parts[1]} in range({parts[5]}, {parts[3]}):\n{indent_spaces}    {parts[1]} = {parts[6]}\n'
            if len(parts) == 6:
                code_python += f'for {parts[1]} in range({parts[5]}, {parts[3]}, 1):\n'
            if len(parts) == 4:
                code_python += f'for {parts[1]} in range(0, {parts[3]}, 1):\n'
            if len(parts) == 2:
                code_python += f'for i in range(0, {parts[1]}, 1):\n'
            if len(parts) == 1:
                code_python += f'while True:\n'

        else:
            print(f"Name '{parts[0]}' is not defined.")
            return
        
    if __name__ == "__main__":
        execute(code, code_python)
    return (code, code_python)



def exit_program():
    return

if __name__ == "__main__":
    code = ''
    while True:
        inp = input()
        if inp == 'run':
            compile(code)
            code = ''
        else:
            code += f'{inp}\n'