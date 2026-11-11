#include <stdio.h>
#include <string.h>
#include <ctype.h>

typedef enum {
    WEAK,
    MEDIUM,
    STRONG
} PasswordStrength;

PasswordStrength checkPassword(const char password[]){
    int upperCase = 0;
    int lowerCase = 0;
    int digit = 0;
    int symbol = 0;

    int length = strlen(password);
    for (int i = 0; i < length; i++)
    {
        unsigned char ch_r = password[i];
        if (isupper(ch_r)) upperCase += 1;
        else if (islower(ch_r)) lowerCase += 1;
        else if (isdigit(ch_r)) digit += 1;
        else symbol += 1;
    }

    // int score = upperCase + lowerCase + digit + symbol;
    printf("\n==========================================\n");
    printf("[-] Password Length [%d] Chars\n", length);
    printf("[-] Password Contains [%d] Upper Letters\n", upperCase);
    printf("[-] Password Contains [%d] Lower Letters\n", lowerCase);
    printf("[-] Password Contains [%d] Numbers\n", digit);
    printf("[-] Password Contains [%d] Symbols\n", symbol);

    if (length > 8 && (upperCase != 0 && lowerCase !=0 && digit !=0 && symbol != 0)){
        return STRONG;
    } 
    else if (length > 8 && (upperCase >= 1 && symbol >= 1) || (lowerCase >= 1 && digit >= 1) || (digit >= 1 && symbol >= 1)){
        return MEDIUM;
    } 
    else{
        return WEAK;
    }  

}

int main(){
    char password[30];
    printf("========== Password Strength Checker ==========\n");
    printf("-> Enter your password: ");
    if (scanf("%29s", password)){
        PasswordStrength result = checkPassword(password);
    
        if (result == STRONG){
            printf("[-] Your Password [%s] is Strong\n", password);
            printf("[-] USE IT\n");
            printf("=========================================\n");
        } 
        else if (result == MEDIUM){
            printf("[-] Your Password [%s] is Medium\n", password);
            printf("[-] MAKE IT TO COMPLEX \n");
            printf("=========================================\n");
        } 
        else{
            printf("[-] Your Password [%s] is Weak\n", password);
            printf("[-] CHANGE IT TO COMPLEX \n");
            printf("=========================================\n");
        } 
    }
    return 0;
}