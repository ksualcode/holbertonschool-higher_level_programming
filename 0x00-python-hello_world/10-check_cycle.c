#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *head, *uwu = list;

	if (list == NULL)
		return(-1);

	head = list;

	for (; uwu;)
	{
		list = uwu;
		uwu = uwu->next;
		if (list <= uwu && uwu >= head)
			return(1);
	}
	return (0);
}
