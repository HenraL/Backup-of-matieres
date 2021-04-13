import random
class root:
    def __init__(self):
        self.alphabet=[' ', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.word_to_sort=""
    def scramble(self):
        b=random.randint(0,len(self.alphabet)**2)
        print(f"b={b}")
        for i in range(b):
            a=alphabet[random.randint(0,len(self.alphabet)-1)]
            self.word_to_sort+=a
            print(f"letter={a},word_to_sort={self.word_to_sort}")
class get(root):
    #def Tupe():.
    #def recursive(self,alphabet_length,spaces,):
    #    .
    #def iterative(self):.
    #def imperative(self):.
    def fibonacci(n):
        if n==0 or n==1:
            return n
        else:
            return (get.fibonacci(n-1)+get.fibonacci(n-2))

RI=root()
print(get.fibonacci(6))

