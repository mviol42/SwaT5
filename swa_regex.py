import re

# these correspond to morpheme slots
P1 = "ha"
P2 = "wa|u|i|ya|vi|zi|u|pa|ku|m|tu|li|ki"
P3 = "si"
P4 = "na|ka|me|sha|taka|li"
P5 = "ye|yo|lo|cho|vyo|zo|po|ko|mo|ye"
P6 = "mw"
P7 = "pend"
P8 = "an|az|i|ian|ik|iki|ikiw|ikiz|ikw|ili|iliw|ish|ishiw|iz|e|ek|ele|ew|esh|" \
     "et|ez|k|lek|lew|li|liw|m|n|ol|sh|shan|s|u|uk|ul|uli|uliw|ush|w|y|z|zik|zw"
P9 = "i"
P10 = "ni"

# 8 more slots are defined to improve performance
PA = "ja"
PB = "ji"
PD = "e"
PE = "a"
PF = "nge|ngeli|ngali"
PG = "ta"
PH = "o"
PJ = "hu"

# combinations of the above morpheme slots

Rule1 = f"^({P1})({P2})?({PA}|{PF}|{PG})?({P6}|{P10}|{PB}|{P2})?({P7})({P8}|{PE}|{PH})?({P9}|{PE})({P10})?$"
Rule2 = f"^({P3})({PA}|{PF}|{PG})?({P2}|{P6}|{PB})?({P7})({P8}|{PE}|{PH})?({P9}|{PD}|{PE})({P10})?$"
Rule3 = f"^({P2}|{PE})({P3}|{P4}|{PF})?({P2}|{P6}|{PB})?({P7})({P8}|{PE}|{PH})?({P9}|{PD}|{PE})({P10})?$"
Rule4 = f"^({P2}|{PE})({P4}|{PF})({P5}|{PH})?({P2}|{P6}|{P10}|{PB})?({P7})({P8}|{PE}|{PH})?({P9}|{PD}|{PE})({P10})?$"
Rule5 = f"^({P2}|{PE})({P4}|{PF}|{PG})?({P2}|{P6}|{P10}|{PB})?({P7})({P8}|{PE}|{PH})?({PE})({P5}|{PH})?({P10})?$"
Rule6 = f"^({P2}|{PE})({P4}|{PF})?({P2}|{P6}|{PB})?({P7})({P8})?({PE})({P5}|{PH})?({P10})?$"
Rule7 = f"^({P7})({P8})?({PE})({P10})?$"
Rule8 = f"^({PJ})({P7})({P8})?({P9}|{PE})$"

if __name__ == '__main__':
    regex = re.compile(f"({Rule1}|"
                       f"{Rule2}|"
                       f"{Rule3}|"
                       f"{Rule4}|"
                       f"{Rule5}|"
                       f"{Rule6}|"
                       f"{Rule7}|"
                       f"{Rule8})")

    # to text each verb, you'll need to change both the verb here and P7 up above (p7 is the root of the verb)
    # feel free to factor this code in anyway if you want to make it more readable/easier to work with
    print([match for match in re.split(regex, 'sipendi') if match])
