# COMP9021 22T3
# Quiz 3 *** Due Friday Week 5 @ 9.00pm
#        *** Late penalty 5% per day
#        *** Not accepted after Monday Week 6 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends and
#   around parentheses and commas, is a valid word.


import sys


def is_valid(word, arity):
#去除空格
    short_word=word.replace(" ", "")

#检测有没有违规的词，不在就不行。
    list1 = ['(', ')', '_', ',']
    for i in range(len(short_word)):
        if not short_word[i].isalpha()  and short_word not  in list1 :
          return False

    #检查左右括号
    m = short_word.count('(')
    n = short_word.count('(')
    if m!=n:
        return False
 # 如果是0的时候不能有括号
    if arity == 0 and m !=0:
        return  False
    if arity == 0 and n !=0 :
        return False

    stack=[]
    temp=''
    temp_str=''
    for i in range(len(word)):
        if short_word [i]=="(":
            stack.append(temp)
            stack.append('(')
        elif word[i]==',':
            stack (temp)
            temp_str=''


            for i in range(arity+1):
                try:
                    temp=stack.pop()
                except:
                    return False
             if temp!='('
        else











    return False
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE









try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')