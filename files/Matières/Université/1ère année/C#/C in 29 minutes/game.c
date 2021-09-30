// small programe, game, guess my number
// open a text editor
// open emacs
// command: emacs -nw game.c
// compiler for c gcc g game.c
// run ./a.out (default name if not specified while compiling)
// to compile a file under a specific name run gcc game.c -o game

#include <stdio.h>
#include <stdlib.h>

int getInput(){
    char input[256]={0};
    read(0,input,256);
    return atoi(input);
}

int main(){
    int outNumber=5;
    // int toGuess=3;
    int toGuess;
    // scanf("%d",&toGuess);
    while (toGuess!=outNumber){
        printf("Please enter a number to guess:");
        toGuess=getInput();
        if (outNumber == toGuess){
            printf("We have the same number!\n");
        } else if (outNumber>toGuess){
            printf("We don't have the same number.\nYour number is bigger than the number to guess.\n");
        } else if (outNumber<toGuess){
            printf("We don't have the same number.\nYour number is smaller than the number to guess.\n");
        };
    };
    printf("I'm alive.\n");

    return 0;
}
