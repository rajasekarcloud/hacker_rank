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
    print(tmsg)

test = "I come to bury Caesar, not to praise him."
transform_message(test,cipher)