#include "forth.h"
#include "words.h"

#include <stdio.h>
#include <string.h>

#define MAX_DATA 16384
#define MAX_STACK 16384
#define MAX_RETURN 16384

int main(int argc, char** argv) {
    FILE* file;
    struct forth forth = {0};
    forth_init(&forth, stdin, MAX_DATA, MAX_STACK, MAX_RETURN);
    words_add(&forth);
    for(int i = 1; i < argc; i++){
        file = fopen(argv[i],"r");
        if(file) {
            forth.input = file;
            forth_run(&forth);
        }
        else{
            if(i == argc - 1 && strcmp(argv[argc - 1], "-") == 0) {
                forth.input = stdin;
                forth_run(&forth);
                continue;
            }
            printf("Can not read file %s\n", argv[i]);
            forth_free(&forth);
            return -1;
        }
    }
    if(argc == 1) {
        forth_run(&forth);   
    }
    forth_free(&forth);
    return 0;
}
