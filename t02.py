"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan Doucet
ID:      181954640
Email:   douc4640@mylaurier.ca
__updated__ = "2019-03-21"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, comparison_total
# import time
# Constants
SEP = '------------------------------------------------------------'
def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
         name - description (type)
    ------------------------------------------------------

    """
    
# start = time.time()
bst1 = BST()
bst2 = BST()
bst3 = BST()

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

for i in DATA1:
    val = Letter(i)
    bst1.insert(val)
for i in DATA2:
    val = Letter(i)
    bst2.insert(val)
for i in DATA3:
    val = Letter(i)
    bst3.insert(val)

test_file = open('otoos610.txt','r',encoding = 'utf-8')
test_file = test_file.read()

do_comparisons(test_file, bst1)
total1 = comparison_total(bst1)

do_comparisons(test_file, bst2)
total2 = comparison_total(bst2)

do_comparisons(test_file, bst3)
total3 = comparison_total(bst3)



print('Comparing by order: {}'.format(DATA1))
print('Total comparisons: {:,}'.format(total1))
print(SEP)
print('Comparing by order: {}'.format(DATA2))
print('Total comparisons: {:,}'.format(total2))
print(SEP)
print('Comparing by order: {}'.format(DATA3))
print('Total comparisons: {:,}'.format(total3))
print(SEP)
print()
# end = time.time()
# time_total = end-start
# print('Took {} to execute'.format(time_total))


    
    