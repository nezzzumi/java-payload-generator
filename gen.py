import sys

string = sys.argv[1]

result = ''

for i, char in enumerate(string):
    code = f'T(java.lang.Character).toString({ord(char)})'

    if i != 0:
        code = '.concat(' + code + ')'

    result += code

print(result)
