#include <stdio.h>
#define CAPACITY 3

int stack[CAPACITY];
int top=-1;

void push(int x){
    if(top<CAPACITY-1){
        top=top+1;
        stack[top]=x;
        printf("Successfully added item %d \n", x);
    }
    else{
        printf("Sorry! No space to add item. \n");
    }
}

int pop(){
    if(top>=0){
        int val=stack[top];
        top=top-1;
        return val;
    }
    return -1;
}

int peek(){
    if (top>=0){
        return stack[top];
    }
    printf("Sorry! Stack is empty to peek.\n");
    return -1;
}

int main()
{
    peek();
    push(5);
    push(10);
    push(15);
    printf("pop item %d \n",pop());
    push(20);
    printf("pop item %d \n",pop());
    
    
    return 0;
}
