# The problem is to create a program that receives a message as input and outputs the sequence of keys that need to be pressed on a Nokia 3310 keypad to type the message.


# Nokia 3310 keypad
key_pad = {
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ',
    0: ' '
}

# Required keys to type the message
required_key = []

message = input().upper()
for char in message:
    for key, value in key_pad.items():
        if char in value:
            required_key.append((value.index(char) + 1) * str(key))
            

print(''.join(required_key))