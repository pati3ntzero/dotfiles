#include<stdio.h>

// A method to compute the quotient, and remainder of
// two integers, and returs the output as a = q*b+r.
int divAlg(long long int, long long int);

int main(int argc, char* argv[]){

    if(argc < 3){ // if there are less than 3 arguments.

        printf("Usage: div <arg1> <arg2>\n"); // print error messege.
        printf("div accepts only exactly 2 arguments.\n");

        return 1; // return error.
    }
    else if(argc > 3){ // if there are two many arguments, see previous case.
        printf("Usage: div <arg1> <arg2>\n"); // print error messege.
        printf("div accepts only exactly 2 arguments.\n");

        return 1;
    }

    // declare long long ints to store possibly large values.
    long long int a;
    long long int b;

    sscanf(argv[1], "%lld", &a); // store arg 1 in a.
    sscanf(argv[2], "%lld", &b); // store arg 2 in b.

    divAlg(a,b); // call the division algorithm on a and b.

    return 0; // return successful if no errors were encountered.
}

int divAlg(long long int a, long long int b){

    if(a < b){ // if a<b
        if(a == 0){ // if a = 0, print error, and return error.
            printf("Division by 0.\n");

            return 1;
        }

        // initialize long long ints for the quotient and the remainder.
        long long int q = b/a; // store floor(b/a) in q.
        long long int r = b%a; // store b mod(a) in r.

        // print the output as b = q*a+r
        printf("%lld = %lld*%lld+%lld\n", b, q, a, r);
    }
    // this condition is the same but with a>= b.
    // See the previous case and switch a with b.
    else if(a >= b){
        if(b == 0){
            printf("Division by 0\n");

            return 1;
        }

        long long int q = a/b;
        long long int r = a%b;

        printf("%lld = %lld*%lld+%lld\n", a, q, b, r);
    }

    return 0; // return success if no errors encountered.
}
