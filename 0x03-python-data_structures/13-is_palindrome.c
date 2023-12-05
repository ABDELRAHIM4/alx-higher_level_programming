#include "lists.h"
#include <stdlib.h>
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *temp;

    slow = *head;
    fast = *head;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        slow = slow->next;
    }

    if (fast != NULL)
        slow = slow->next;

    while (slow != NULL)
    {
        if (slow->n != (*head)->n)
            return (0);
        slow = slow->next;
        temp = *head;
        *head = (*head)->next;
        free(temp);
    }

    return (1);
}
