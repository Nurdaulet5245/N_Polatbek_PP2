def defangIPaddr(address: str) -> str:
    print(address.replace('.', '[.]'))

n = input()

defangIPaddr(n)