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
    RAND = False
    MATH = False
    TIME = False
    code = code.split('\n')
    code_python = ''
    splited_python_code = code_python.split('\n')
    i = 0
    for line in code:

        stripped_line = line.strip()
        if not stripped_line:
            i += 1
            continue

        indent_level = len(line) - len(line.lstrip())

        if indent_level % 4 != 0:
            raise TabError('Invalid indent level. Expected multiple of 4.')

        indent_spaces = ' ' * indent_level

        code_python += indent_spaces
        splited_python_code = code_python.split('\n')

        parts = stripped_line.split(' ')
        # command = parts[0]

        # prints
        if parts[0] == 'output': # output Hello World
            result = ' '.join(parts[1:])
            code_python += f'print(\'{result}\')\n'
        elif parts[0] == 'outputf': # outputf <x>
            print_result = ' '.join(parts[1:])
            result = print_result.replace('<', '{').replace('>', '}')
            code_python += f'print(f\'{result}\')\n'
            splited_python_code = code_python.split('\n')

        elif parts[0] == '///': # output Hello World
            result = ' '.join(parts[1:])
            code_python += f'# {result}\n'

        # variables
        elif parts[0] == 'input': # input x
            code_python += f'{parts[1]} = input()\n'
        elif parts[0] == 'var': # check x == y
            if parts[1] == 'str' or parts[1] == 'string': # var str x "Hello World"
                result = ' '.join(parts[2:])
                result = result.replace('<', '{').replace('>', '}')
                code_python += f'{parts[2]} = f"{result}"\n'
            elif parts[1] == 'dec' or parts[1] == 'decimal': # var dec x 10.5
                code_python += f'{parts[2]} = float({parts[-1]})\n'
            elif parts[1] == 'int' or parts[1] == 'integer': # var num x 10
                code_python += f'{parts[2]} = int({parts[-1]})\n'
            elif parts[1] == 'arv' or parts[1] == 'arrive': # var arv x 1 2 3...
                if len(parts) <= 3:
                    code_python += f'{parts[2]} = []\n'
                else:
                    result = ', '.join(parts[3:])
                    result = result.replace('<', '{').replace('>', '}')
                    code_python += f'{parts[2]} = [{result}]\n'

            elif parts[1] == 'func' or parts[1] == 'function': # var func x func_name arg1 arg2...
                result = ''
                if len(parts) <= 4:
                    code_python += f'{parts[2]} = {parts[3]}()\n'

                # functions
                if parts[3] == 'rand': # var func x rand 1 100
                    if RAND == False:
                        code_python = 'import random\n' + code_python
                        RAND = True
                    code_python += f'{parts[2]} = random.randint({parts[4]}, {parts[5]})\n'
                    
                elif parts[3] == 'lenght':
                    result = ' '.join(parts[4:])
                    result = result.replace('<', '{').replace('>', '}')
                    code_python += f'{parts[2]} = len(f"{result}")\n'

                elif parts[3] == 'lowercase':
                    result = ' '.join(parts[4:])
                    result = result.replace('<', '{').replace('>', '}')
                    code_python += f'{parts[2]} = f"{result}".lower()\n'

                elif parts[3] == 'uppercase':
                    result = ' '.join(parts[4:])
                    result = result.replace('<', '{').replace('>', '}')
                    code_python += f'{parts[2]} = f"{result}".upper()\n'

                elif parts[3] == 'root': # var func x squareroot 16
                    if MATH == False:
                        code_python = 'import math\n' + code_python
                        MATH = True
                    code_python += f'{parts[2]} = math.sqrt({parts[-1]})\n'

                elif parts[3] == 'fact': # var func x squareroot 16
                    if MATH == False:
                        code_python = 'import math\n' + code_python
                        MATH = True
                    result = ' '.join(parts[4:])
                    code_python += f'{parts[2]} = math.factorial({parts[-1]})\n'

                elif parts[3] == 'read': # var func x read arrive 0
                    code_python += f'{parts[2]} = {parts[4]}[{parts[-1]}]\n'

                else:
                    for j in parts[4:]:
                        result += f'{j}, '
                    result = result[:-2]
                    code_python += f'{parts[2]} = {parts[3]}({result})\n'

            else:
                code_python += f'{parts[1]} = {parts[-1]}\n'

        # conditions
        elif parts[0] == 'is': # is x = y type
            if parts[2] == '=': parts[2] = '=='
            if len(parts) >= 5:
                if parts[4] == 'str' or parts[4] == 'string':
                    code_python += f'if {parts[1]} {parts[2]} \'{parts[3]}\':\n'
            else:
                code_python += f'if {parts[1]} {parts[2]} {parts[3]}:\n'

        elif parts[0] == 'also': # also x == y
            if parts[2] == '=': parts[2] = '=='
            if len(parts) >= 5:
                if parts[4] == 'str' or parts[4] =='string':
                    code_python += f'elif {parts[1]} {parts[2]} \'{parts[3]}\':\n'
            else:
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

        # cycle operators
        elif parts[0] == 'exit':
            code_python += f'break\n'
        elif parts[0] == 'repeat':
            code_python += f'continue\n'

        # functions
        elif parts[0] == 'func': # func name
            if i + 1 < len(code) and code[i + 1].strip().startswith('args') or code[i + 1].strip().startswith('args'): # args x y
                args = ', '.join(code[i + 1].strip().split(' ')[1:])
                code_python += f'def {parts[1]}({args}):\n'
                i += 1
                line = code[i].strip()
                continue 
            else:
                print(i + 1 < len(code))
                print(code[i + 1].strip().startswith('args'))
                print(code[i + 1].strip())
                print(code[i + 1])
                code_python += f'def {parts[1]}():\n'
            splited_python_code = code_python.split('\n')

        elif parts[0] == 'call': # call func_name x y
            if parts[1] == 'wait': # call wait x
                if TIME == False:
                    code_python = 'import time\n' + code_python
                    TIME = True
                result = parts[-1].replace('<', '{').replace('>', '}')
                code_python += f'time.sleep({result} / 1000)\n'

            elif parts[1] == 'add': # call add arrive x
                code_python += f'{parts[2]}.append({parts[-1]})\n'
                continue
                
            elif parts[1] == 'addstr': # call addstr arrive hello world
                result = ' '.join(parts[2:]).replace('<', '{').replace('>', '}')
                code_python += f'{parts[2]}.append("{result}")\n'
                continue

            elif parts[1] == 'remove': # call remove arrive 0
                code_python += f'{parts[2]}.pop({parts[3]})\n'
                continue

            elif parts[1] == 'write': # call write arrive 0 5
                code_python += f'{parts[2]}[{parts[3]}] = {parts[-1]}\n'
                continue

            elif parts[1] == 'writestr': # call write arrive 0 5
                result = ' '.join(parts[4:]).replace('<', '{').replace('>', '}')
                code_python += f'{parts[2]}[{parts[3]}] = f"{result}"\n'
                continue

            if len(parts) <= 2:
                code_python += f'{parts[1]}()\n'
            else:
                args = ', '.join(parts[2:])
                code_python += f'{parts[1]}({args})\n'

        elif parts[0] == 'args': # args x y
            code_python += '\n'

        elif parts[0] == 'back': # back x
            code_python += f'return {parts[1]}\n'

        # exceptions
        elif parts[0] == 'incase': # incase
            code_python += f'try:\n'

        elif parts[0] == 'occurred': # occurred x
            if len(parts) >= 3 and parts[1] == 'error':
                code_python += f'except {parts[-1]}:\n'
            code_python += f'except Exception as {parts[1]}:\n'


        # else:
        #     print(f"Name '{parts[0]}' is not defined.")
        #     return
        

        i += 1




    if __name__ == "__main__":
        execute(code, code_python)
    return (code, code_python)



def exit_code():
    quit()

if __name__ == "__main__":
    code = ''
    while True:
        inp = input()
        if inp == 'run':
            compile(code)
            code = ''
        else:
            code += f'{inp}\n'