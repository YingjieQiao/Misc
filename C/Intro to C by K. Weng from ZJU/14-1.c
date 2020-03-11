#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct LNODE *Lnode;
struct LNODE
{
    int data;
    Lnode next;
    Lnode last;
};

typedef struct LIST *List;
struct LIST
{
    Lnode head;
    Lnode tail;
};

int main(int argc, char const *argv[]) {
  List L;
    L = (List)malloc(sizeof(struct LIST));
    L->head = L->tail = NULL;
    int d;
    scanf("%d", &d);
    Lnode temp;
    int first = 1;
    while (d != -1)
    {
        temp = (Lnode)malloc(sizeof(struct LNODE));
        temp->data = d;
        temp->next = NULL;
        if (first)
        {
            temp->last = NULL;
            first = 0;
            L->head = temp;
            L->tail = temp;
        }
        else
        {
            temp->last = L->tail;
            //L->tail->next = temp;
            L->tail = temp;
        }
        scanf("%d", &d);
    }
    for (temp = L->tail; temp; temp = temp->last)
    {
        printf("%d ", temp->data);
    }
    putchar('\n');
    Lnode p;
    for (p = L->head; p;)
    {
        temp = p;
        p = p->next;
        free(temp);
    }
    return 0;
}
