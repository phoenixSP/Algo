# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 20:24:02 2019

@author: shrey
"""

class Decompress:
    def __init__(self, string):
        self.string=string
    """
    Check is_valid(string) first
    Read the string iteratively. While 
    1) If char is number, store it in number_buffer
    2) if char is letter, store it in string_buffer
    3) if char is opening bracket, then push the number in number buffer to the stack, clear number_buffer, increase count_open
    4) if char is closing bracket, then push the string in string buffer to the stack, clear string_buffer,, increase closing bracket count. 
    Read the stack till a number is encountered, and evaluate the string. Push the evaluated string again in the stack
    
    when end of the string is reached, check if the number of opening and closing brackets are the same. stack should contain
    all strings. concatenate all of them.

    """    
    
    def is_valid(self):
        if self.string is None or len(self.string)==0 or self.string[0].isalpha() or self.string[0]==0:
            print("Here 1")
            return False
        else:
            count_open=0
            count_closed=0
            for char in self.string:
                if char=="[":
                    count_open+=1
                elif char=="]":
                    count_closed+=1
                    
            if count_open!=count_closed:
                print("Here 2")
                return False
        return True
        
    def decompress(self):
        if not self.is_valid():
            print("Enter valid string")
            return 
                    
        number_buffer=""
        string_buffer=""
        count_open=count_closed=0
        stack=[]
        output=""
        for char in self.string:
            if char.isdigit():
                number_buffer+=char
            elif char.isalpha():
                string_buffer+=char
            elif char=="[":
                stack.append(number_buffer)
                number_buffer=""
                count_open+=1
            elif char=="]":
                stack.append(string_buffer)
                string_buffer=""
                count_closed+=1
                while not stack[-1].isdigit():
                    output=stack.pop(-1)+output
                output=int(stack.pop(-1))*output
                stack.append(output)
                output=""
                
        while len(stack)!=0:
            output=stack.pop(-1)+output
            
        print(output)
        
string=Decompress("2[2[ab]e]3[cd]")
string.decompress()

        

                
            
            
            