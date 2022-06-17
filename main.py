"""
Name(s):Casper Smith, Evan Schleck
Name of Project: Los "Mad Libs" de Azucar 
"""

#Write the main part of your program here. Use of the other pages is optional.

import random

stories = [1, 2, 3, 4]
f = random.choice(stories)
print(f)
if f == 1:
    import page1
elif f == 2:
    import page2
elif f == 3:
    import page3
elif f == 4:
    import page4
