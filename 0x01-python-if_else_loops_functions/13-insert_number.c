#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *temp;
new_node = malloc(sizeof(listint_t));
if (!new_node)
return (NULL);
new_node->n = number;
new_node->next = NULL;
if (!*head || number < (*head)->n)
{
new_node->next = *head;
*head = new_node;
return (new_node);
}
temp = *head;
while (temp->next && number > temp->next->n)
temp = temp->next;
new_node->next = temp->next;
temp->next = new_node;
return (new_node);
}
