# include <stdio.h>

int main() {
    int a = 3;
    int b = 4;
    int i;
    if(a > b) {
      i = b;
        b = a;
        a = i;
    }
    printf("c: a=%d, b=%d\n", a, b);
    return 0;
}