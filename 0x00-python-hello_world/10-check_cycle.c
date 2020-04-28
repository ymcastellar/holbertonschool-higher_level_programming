#include "lists.h"

/**
 * check_cycle - checks if has a cycle
 * @list: parameter pointer to
 * Return: 1 exits, 0 not exits
 */

int check_cycle(listint_t *list)
{
	listint_t *fnode = list, *snode = list;

	while (snode && snode->next)
	{
		fnode = fnode->next;
		snode = snode->next->next;
		if (fnode == snode)
			return (1);
	}
	return (0);
}
