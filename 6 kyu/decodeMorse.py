def decodeMorse(morse_code):
    code = [c.split(' ') for c in morse_code.strip().split('   ')]
    code = ' '.join([''.join([MORSE_CODE[char] for char in word]) for word in code])
    return(code)

# morse = "ttt ooo   bbb eee   sos"
# def decodeMorse(morse_code):
# 	MORSE_CODE = {'ttt':'t', 'ooo':'o', 'bbb':'b', 'eee':'e', 'sos':'sos'}

# 	morse_code = [char.split(' ') for char in morse_code.strip().split('   ')]
# 	morse_code = ' '.join([''.join([MORSE_CODE[char] for char in word]) for word in morse_code])

# 	return(morse_code)

# print(decodeMorse(morse))
# return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')