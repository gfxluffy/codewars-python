word_to_num = {'zero'     : 0,
               'one'      : 1,
               'two'      : 2,
               'three'    : 3,
               'four'     : 4,
               'five'     : 5,
               'six'      : 6,
               'seven'    : 7,
               'eight'    : 8,
               'nine'     : 9,
               'ten'      : 10,
               'eleven'   : 11,
               'twelve'   : 12,
               'thirteen' : 13,
               'fourteen' : 14,
               'fifteen'  : 15,
               'sixteen'  : 16,
               'seventeen': 17,
               'eighteen' : 18,
               'nineteen' : 19,
               'twenty'   : 20,
               'thirty'   : 30,
               'forty'    : 40,
               'fifty'    : 50,
               'sixty'    : 60,
               'seventy'  : 70,
               'eighty'   : 80,
               'ninety'   : 90
              }

def parse_3(string):
    
    e_o = string
    number = 0
    
    if 'hundred' in string:
        h, e_o = string.split(' hundred')
        number += word_to_num[h] * 100
        if string.endswith(' hundred'):
            return number
        
    if '-' in e_o:
        e, o = e_o.strip().split('-')
        number += word_to_num[e] + word_to_num[o]
        
    else:
        number += word_to_num[e_o.strip()]
        
    return number
    
def parse_int(string):
    
    number = 0
    string = string.replace(' and', '')
    rvalues = string
    print(string)
    
    if 'million' in string:
        m, rvalues = string.split(' million')
        number += parse_3(m) * 1000000
        if string.endswith(' million'):
            return number
        
    if 'thousand' in rvalues:
        t, rvalues = rvalues.strip().split(' thousand')
        number += parse_3(t) * 1000
        if rvalues.endswith(' thousand'):
            return number
    
    if rvalues:
        number += parse_3(rvalues.strip())
    
    return number