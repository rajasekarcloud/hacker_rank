# transform_message('Hello', {'H':'I','l':'m'}) returns 'Iemmo'

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
cipher = {letters[i]: letters[(i-3) % len(letters)] for i in range(len(letters))}

def transform_message(message, cipher):
    tmsg=""
    for i in message:
        if cipher.get(i):
            tmsg = tmsg+cipher.get(i)
        else:
            tmsg = tmsg + i
    return (tmsg)
def transform_message_1(test_encoded,decoder):
    result = ''
    for char in test_encoded:
        if char.isalpha():
            if char.isupper():
                upper_key=char
                result = result + decoder.get(upper_key)
            else:
                lower_key=char
                result = result + decoder.get(lower_key)
        elif char == ",":
            result = result + ","
        elif char == ".":
            result = result + "."
        else:
            result = result + " "
    return result

test = "I come to bury Caesar, not to praise him."
test_encoded=str(transform_message(test,cipher))
test_encoded='F Zljb ql Yrov zXbpXo, klq ql moXfpb efj.'
print(cipher)
decoder = {v: k for k, v in cipher.items()}
print(decoder)
print(transform_message_1(test_encoded, decoder))
