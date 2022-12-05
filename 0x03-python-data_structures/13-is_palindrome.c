#include "lists.h"

/**
 * reverse_list - Function that reverses a list
 * @head: pointer to pointer to beginnig of list to be reversed
 *
 * Return: nothing
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_list - function to compare elements of a list
 * @firstHalf: pointer to first half of a list
 * @secondHalf: pointer to second half of list
 *
 * Return: 0 if list is not palindrome otherwise 1
 */
int compare_list(listint_t *first_half, listint_t *second_half)
{
	while (first_half && second_half)
	{
		if (first_half->n != second_half->n)
			return (0);
		first_half = first_half->next;
		second_half = second_half->next;
	}
	return (1);
}

/**
 * is_palindrome - Function in C that checks if a singly linked list
 * 		is a palindrome
 * @head: pointer to to pointer to head of list
 * Return: 0 if list is not palindrome otherwise 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast_ptr, *prev_of_slow_ptr, *slow_ptr, *mid_ptr;
	listint_t *firstHalf_ptr, *secondHalf_ptr;
	int res;

	if ((head == NULL) || (*head == NULL))
		return (1);

	fast_ptr = prev_of_slow_ptr = slow_ptr = firstHalf_ptr = *head;
	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;

		prev_of_slow_ptr = slow_ptr;
		slow_ptr = slow_ptr->next;
	}
	if (fast_ptr != NULL)
	{
		mid_ptr = slow_ptr;
		secondHalf_ptr = mid_ptr->next;
	}
	else
		secondHalf_ptr = slow_ptr;

	prev_of_slow_ptr->next = NULL;
	reverse_list(&secondHalf_ptr);
	res = compare_list(firstHalf_ptr, secondHalf_ptr);

	reverse_list(&(secondHalf_ptr));
	if (fast_ptr != NULL)
	{
		prev_of_slow_ptr->next = mid_ptr;
		mid_ptr->next = secondHalf_ptr;
	}
	else
		prev_of_slow_ptr->next = secondHalf_ptr;

	return (res);
}
