#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function that inserts a number into a sorted singly
 * linked list
 * @head: pointer of pointer to head of list
 * @number: number to be inserted
 *
 * Return: address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *copy, *new;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	copy = *head;
	if ((*head == NULL) || (number <= (*head)->n))
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while ((copy && copy->next) && (number > (copy->next)->n))
		copy = copy->next;

	new->next = copy->next;
	copy->next = new;

	return (new);
}
