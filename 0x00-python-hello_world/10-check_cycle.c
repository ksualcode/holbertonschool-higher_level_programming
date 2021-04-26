#include "lists.h"

/**
* check_cycle - Checks if the list cycles
* @list: list to evaluate
* ------------------------------------------------
* Return: 1 if cycles, 0 if not
*/
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
