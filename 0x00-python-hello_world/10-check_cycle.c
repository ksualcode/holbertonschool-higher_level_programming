#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *uwu = list;

	if (list == NULL)
		return(-1);

	for (; uwu;)
	{
		list = uwu;
		uwu = uwu->next;
		if (list <= uwu)
			return(1);
	}
	return (0);
}
