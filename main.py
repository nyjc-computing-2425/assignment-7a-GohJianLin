# Write a function to convert numbers to text numerals

def text_numeral(num):
  """
  converts numerical value num into text form.
  
  Parameters
  ----------
  num
    a numerical value ranging from 1 to 99

  Returns
  -------
  text
    text form of the numerical value given

  Example:
  >>> text_numeral(15)
  'fifteen'
  >>> text_numeral(29)
  'twenty nine'
  """
  NUM_WORD= {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety'
  }
  temp = []
  k = -1 #index of number from last 
  while num != 0:
    a = list(NUM_WORD.keys())[k]
    if num >= a :
      num -= a
      temp += [NUM_WORD[a]]
    elif num < a:
      k -= 1
  if num == 0 :
    return ' '.join(temp)