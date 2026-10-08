#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "libs/listgen.h"
#include "libs/listfun.h"

int find(int query, sadish *list)
{
    while (list != NULL)
    {
        if (list->data == query)
            return 1;

        list = list->next;
    }

    return 0;
}

sadish *insert(sadish *head, double data)
{
    sadish *newnode = malloc(sizeof(sadish));

    newnode->data = data;
    newnode->next = NULL;

    if (head == NULL)
        return newnode;

    sadish *temp = head;

    while (temp->next != NULL)
        temp = temp->next;

    temp->next = newnode;

    return head;
}

void printSadish(sadish *head)
{
    while (head != NULL)
    {
        printf("%.0f ", head->data);
        head = head->next;
    }

    printf("\n");
}

int main()
{
    sadish *L1 = NULL;
    sadish *L2 = NULL;

    int a[] = {1, 7, 12, 3, 9, 5, 11, 15, 8};
    int b[] = {1, 11, 6, 9, 15, 12, 4};

    for (int i = 0; i < 9; i++)
        L1 = insert(L1, a[i]);

    for (int i = 0; i < 7; i++)
        L2 = insert(L2, b[i]);

    printf("L1 before: ");
    printSadish(L1);

    printf("L2:        ");
    printSadish(L2);

    sadish *ptr1 = L1;

    while (ptr1->next != NULL)
    {
        int query = ptr1->next->data;

        if (find(query, L2))
        {
            ptr1->next = ptr1->next->next;
        }
        else
        {
            ptr1 = ptr1->next;
        }
    }

    printf("L1 after:  ");
    printSadish(L1);

    return 0;
}
