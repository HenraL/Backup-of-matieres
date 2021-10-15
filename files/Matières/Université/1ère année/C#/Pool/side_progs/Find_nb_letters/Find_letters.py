#!/usr/bin/env python3 
def open_file(file): #equivalent to the initialisation of the elements that will need to be searched by the program.
    f=open(file,"r")
    content=f.read()
    f.close()
    return content # same

def my_putchar(word): #<=> var my_putchar(char word) {
    print(word,end="") # <=> my_putchar(1,word,1);
#                        <=> }

def separate_all_characters(file_content): # <=> chr separate_all_characters(chr file_content)
    file_content_length = len(file_content) # <=> int file_content_length = my_str_len(file_content_length);
    nb_f_c_index = 0 # <=> setting the index for the while
    f_c_result = [] # <=> int ch_nb_result[];
    while ( nb_f_c_index < file_content_length ) :
        f_c_result.append(file_content[nb_f_c_index]) # <=> ch_nb_result[nb_ch_index] = file_content[nb_f_c_index];
        nb_f_c_index += 1 # <=> nb_ch_index++;
    return f_c_result #same

def count_wished_charater(file_content,character): #char count_wished_charater(char file_content, char character)
    i = 0 #<=> int i = 0;
    list_length=len(file_content) # <=> int list_length = my_str_len(file_content);
    nb_times=0 #<=> int nb_times = 0;
    while (i < list_length): #same
        if (file_content[i] == character) : #same
            nb_times+=1 #same
        i+=1 # i++
    return nb_times
    
def start_search(ch_list,charaters): # <=> char start_search(chr ch_list, chr charaters)
    ch_length = len(charaters) # <=> int ch_length = my_str_len(characters or ch_list);
    nb_ch_index = 0 # <=> setting the index for the while
    ch_nb_result = [] # <=> int ch_nb_result[];
    temp_result = 0 # <=> int temp_result = 0;
    while ( nb_ch_index < ch_length ) :
        temp_result=count_wished_charater(ch_list,charaters[nb_ch_index]) # <=> temp_result = wished_character(ch_list[nb_ch_index]);
        ch_nb_result.append(temp_result) # <=> ch_nb_result[nb_ch_index] = temp_result;
        nb_ch_index += 1 # <=> nb_ch_index++;
    return ch_nb_result
    
def main(file_path_and_name,charaters):
    file_content_list = separate_all_characters(file_content) #<=> char file_content_list = separate_all_characters(file_content);
    # ch_list = charaters.split(",") #This is only necessary if given in a non list form, see higher up for more info on this line in c
    nb_characters = start_search(file_content_list,charaters) #<=> int nb_characters[] = start_search(file_content_list, ch_list);
    nb_display=0 # <=> int nb_display = 0;
    nb_display_length = len(nb_characters) # <=> int nb_display_length = my_str_len(nb_characters);
    while (nb_display < nb_display_length) : #same (just replace : by {)
        my_putchar(charaters[nb_display]) # replace by my_put_str(characters[nb_display]);
        my_putchar(':') #just add a ;
        my_putchar(nb_characters[nb_display]) # replace by my_put_str(nb_characters[nb_display]);
        my_putchar('\n') #<=> my_putchar(10);
        nb_display+=1 # <=> nb_display++;
    return charaters, nb_characters

file_content = open_file("Test.txt") # <=> chr file_content = open_file(file_path_and_name);
#This a very long list of characters to test.
charaters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","u","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","&","é","\"","#","&","~","{","}","(",")","[","]","-","|","`","è","\\","_","ç","^","à","@","°",")","+","=","£","$","¤","µ","*","%","ù","?",",",".",";","/",":","§","!","<",">","²"]
main(file_content,charaters) #calling the main, the way the one in c will be called, will have to be deduced from the rush.