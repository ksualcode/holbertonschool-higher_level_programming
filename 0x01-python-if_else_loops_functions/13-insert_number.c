#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
* insert_node - Inserts a node in a list
* @head: head of a linked list
* @number: Node where is the new node needed
* ---------------------------------------------
* Return: return a pointer the new node or a null if failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *temp = *head;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	else if ((*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	for (; temp;)
	{
		if ((temp->next == NULL || temp->next->n > number))
		{
			if (temp->next == NULL)
				new_node->next = NULL;
			else
				new_node->next = temp->next;
			temp->next = new_node;
			return (new_node);
		}

		temp = temp->next;
	}

	return (NULL);
}
