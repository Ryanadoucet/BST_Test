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
# Constants

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
    
def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains 
    the number of comparisons found by searching for that Letter 
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects 
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in file_variable:
        if i.isalpha():
            i = i.upper()
            i = Letter(i)
            bst.retrieve(i)
    
    return
def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    a = bst.inorder()
    for i in a:
        total += i.comparisons
    return total

def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    total = comparison_total(bst)
    a = bst.inorder()
#     count_total = 0
#     for i in a:
#         count_total += i.count
    print('Letter Count/Percent Table')
    print()
    print('Total Count: {:,}'.format(total))
    print()
    print('{:<8s}{:<5s}{:>8s}'.format('Letter','Count','%'))
    print('-'*21)
    for i in a:
        percentage = (i.count/total) * 100 
        print('{:>5s}  {:<6}   {:<4.2f}%'.format(i.letter,i.count,percentage))
    