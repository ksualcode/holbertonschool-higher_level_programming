#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: head of a list
 *
 * Return: pointer to head of new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	for (;current;)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * is_palindrome - checks if a linked list palindrome
 * @head: head of a linked list
 *
 * Return: 1 if success, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	for (;1;)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&dup);

	while (dup && *head)
	{
		if ((*head)->n == dup->n)
		{
			dup = dup->next;
			*head = (*head)->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}