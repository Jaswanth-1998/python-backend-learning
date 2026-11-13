'''
def isPhoneNumber(text):
 if len(text) != 12:
    return False
 for i in range(0, 3):
    if not text[i].isdecimal():
     return False
 if text[3] != '-':
    return False
 for i in range(4, 7):
    if not text[i].isdecimal():
        return False
 if text[7] != '-':
    return False
 for i in range(8, 12):
    if not text[i].isdecimal():
        return False
 return True
print('4155554242 is a phone number:')
print(isPhoneNumber('4155554242'))
print('Jaswanth is a phone number:')
print(isPhoneNumber('Moshi moshi'))
'''

def isPhoneNumber(text):
   if len(text) != 10:
      return False
   for i in range(0,10):
      if not text[i].isdecimal():
         return False
   return True
print('7339553262 is a phone number:', isPhoneNumber('7339553262'))
print('abcdefghij is a phone number:', isPhoneNumber('abcdefghij'))

msg = 'Call me at 7339553262 tomorrow. 73395532 is my office number.'
for i in range(len(msg)):
   chunk = msg[i:i+10]
   if isPhoneNumber(chunk):
      print('Phone number found: ' + chunk)
print('Done')