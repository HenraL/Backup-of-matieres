import random
def pause():pause=input("Press enter to continue...")
class root:
    def __init__(self):
        self.alphabet=[' ', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.word_to_sort=[]
        self.letter_counter={}
    def initialises_more_complex_vars(self):
        for i in range(len(self.alphabet)):
            if (str(self.alphabet[i]).lower() not in self.letter_counter) and (self.alphabet[i]!=" "):
                self.letter_counter[self.alphabet[i].lower()]=0
    def scramble(self):
        self.word_to_sort=[]
        for i in self.letter_counter:
            self.letter_counter[i]=0
        b=random.randint(0,len(self.alphabet)**2)
        print(f"b={b}")
        for i in range(b):
            a=self.alphabet[random.randint(0,len(self.alphabet)-1)]
            self.word_to_sort.append(a)
            #print(f"letter={a},word_to_sort={self.word_to_sort}")
        print(f"word_to_sort={self.word_to_sort}")
class get(root):
    def display(dicti):
        for i in dicti:
            print(f"dicti[{i}]={dicti[i]}")
    def Tupe(self,tupe,n=0):
        if tupe==1:
            root.scramble(self)
            print(get.recursive(self,alphabet_length=len(self.alphabet),spaces=0,current_index=0))
        elif tupe==4:
            print("Calculating...")
            e=get.fibonacci_rec(n)
            print("Done")
            print(f"result={e}")
        elif tupe==5:
            print("Calculating...")
            e=get.fibonacci_it(n)
            print("Done")
            print(f"result={e[2]}")
        print(f"{chr(169)} Created By Henry Letellier")
    
    def recursive(self,alphabet_length,spaces=0,current_index=0):
        if alphabet_length>0:
            if current_index==alphabet_length:
                print("alphabet_length=",alphabet_length)
                print("spaces=",spaces)
                print("current_index=",current_index)
                get.display(self.letter_counter)
                return "Finished"
            elif self.word_to_sort[current_index]==" ":
                return get.recursive(self,alphabet_length,spaces+1,current_index+1)
            else:
                self.letter_counter[self.word_to_sort[current_index].lower()]+=1
                return get.recursive(self,alphabet_length,spaces,current_index+1)
        else:
            return "There is nothing to treat, length of string = 0"
    #def iterative(self):.
    #def imperative(self):.
    def fibonacci_rec(n):
        #print(f"n={n}")
        if n==0 or n==1:
            return n
        else:
            return (get.fibonacci_rec(n-1)+get.fibonacci_rec(n-2))
    def fibonacci_it(n):
        if n==0 or n==1:
            return n
        else:
            i=0
            numbers=[0,1]
            while n>=1:
                numbers.append(numbers[i]+numbers[i+1])
                #print(f"numbers[i]={numbers[i]}\nnumbers[len(numbers)-1]={numbers[len(numbers)-1]}")
                i+=1
                n-=1
            #print(f"i={i},n={n},numbers={numbers},numbers[len(numbers)-1]={numbers[len(numbers)-1]}")
        return n, numbers,i

RI=root()
root.initialises_more_complex_vars(RI)
get.Tupe(RI,4,6)
get.Tupe(RI,1)
get.Tupe(RI,4,int(input("Enter a whole number greater than 1:")))
get.Tupe(RI,5,int(input("Enter a whole number greater than 1:")))
pause()
