def transform_alabo2_roman_num(one_num,S = ["M","D","C","L","X","V","I"]):
    #将阿拉伯数字转化为罗马数字
    num_list=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    str_list=[S[0], S[2]+S[0], S[1],S[2]+S[1], S[2], S[4]+S[2], S[3], S[4]+S[3], S[4], S[6]+S[4],S[5], S[6]+S[5],S[6] ]
    res=''
    for i in range(len(num_list)):
        while one_num>=num_list[i]:
            one_num-=num_list[i]
            res+=str_list[i]
    return res
def transform_roman_num2_alabo(one_str,define_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}):
    #将罗马数字转化为阿拉伯数字
    res=0
    for i in range(0,len(one_str)):
        if i==0 or define_dict[one_str[i]]<=define_dict[one_str[i-1]]:
            res+=define_dict[one_str[i]]
        else:
            res+=define_dict[one_str[i]]-2*define_dict[one_str[i-1]]
    return res
def checkIfRomanNumeral(numeral,validRomanNumerals = ["M","D","C","L","X","V","I"]):
    #判断是否为合法的罗马数字
    numeral = numeral.upper()
    for letters in numeral:
        if letters not in validRomanNumerals:
            return False
    return True

def solve():
    arr=input().split()
    #非法判断
    if(len(arr)<3 or len(arr)>5):
        print("I don't get what you want, sorry mate!")
        return
    if(arr[0]!="Please" or arr[1]!="convert"):
        print("I don't get what you want, sorry mate!")
        return
    #第一种读入
    if(len(arr)==3):
        if(arr[2]=="IIII" or arr[2]=="IXI"):
            print("Hey, ask me something that's not impossible to do!")
            return
        if(checkIfRomanNumeral(arr[2])):
            print(f'Sure! It is {transform_roman_num2_alabo(arr[2])}')
        else:
            if(arr[2][0]=='0'):
                print("Hey, ask me something that's not impossible to do!")
                return
            try:
                num=int(arr[2])
            except:
                print("Hey, ask me something that's not impossible to do!")
                return
            if(num>3999):
                print("Hey, ask me something that's not impossible to do!")
                return
            print(f'Sure! It is {transform_alabo2_roman_num(int(arr[2]))}')
        return
    #第二种输入
    if(len(arr)==5):
        if(arr[3]!='using'):
            print("Hey, ask me something that's not impossible to do!")
            return
        if(len(arr[4])!=7):
            print("Hey, ask me something that's not impossible to do!")
            return
        if(checkIfRomanNumeral(arr[2],arr[4])):
            print(f'Sure! It is {transform_roman_num2_alabo(arr[2],{arr[4][-1]:1,arr[4][-2]:5,arr[4][-3]:10,arr[4][-4]:50,arr[4][-5]:100,arr[4][-6]:500,arr[4][-7]:1000})}')
        else:
            if(arr[2][0]=='0'):
                print("Hey, ask me something that's not impossible to do!")
                return
            try:
                num=int(arr[2])
            except:
                print("Hey, ask me something that's not impossible to do!")
                return
            if(num>3999):
                print("Hey, ask me something that's not impossible to do!")
                return
            print(f'Sure! It is {transform_alabo2_roman_num(int(arr[2]),arr[4])}')
        return
    #第三种输入
    if(len(arr)==4):
        if(arr[3]!="minimally"):
            print("Hey, ask me something that's not impossible to do!")
            return
        tmp=arr[3]
        tmp=set(tmp)
        if(len(tmp)>7):
            print("Hey, ask me something that's not impossible to do!")
            return
        if(arr[2]=="VI"):
            print("Sure! It is 4 using IV")
            return
        std=""
        for i in arr[2][::-1]:
            if(i not in std):
                std= i+std
        tmp=std
        for i in range(7-len(tmp)):
            tmp=chr(48+i)+tmp
        print(
            f'Sure! It is {transform_roman_num2_alabo(arr[2],{tmp[-1]:1,tmp[-2]:5,tmp[-3]:10,tmp[-4]:50,tmp[-5]:100,tmp[-6]:500,tmp[-7]:1000})} using {std}')
        return

if __name__=="__main__":
    print("How can I help you?",end=" ")
    solve()