def interpret(command: str) -> str:
    command = command.replace('()', 'o')
    print(command.replace('(al)', 'al'))
n = input()

interpret(n)