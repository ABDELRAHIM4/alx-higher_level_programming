#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @head: pointer to list to be checked
 * Return: 1 if a cycle is found, 0 if no cycle is found, -1 if an error occurs
 */
int check_cycle(listint_t *head)
{
listint_t *tortoise, *hare;

if (head == NULL)
return (-1);

tortoise = head;
hare = head;
while (hare != NULL && hare->next != NULL)
{    
tortoise = tortoise->next;
hare = hare->next->next;
if (tortoise == hare)
return (1);
}
return (0);
}
