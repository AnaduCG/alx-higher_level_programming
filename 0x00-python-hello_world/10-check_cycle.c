#include "lists.h"
/**
 *check_cycle - function that checks if a
 *		linked list has an infinite loop in it
 *@list: pointer to the first node of the linked list
 *Return: returns 1 if any is found and 0 otherwise
 *
 *
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);
	slow = list;
	fast = list->next;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
			return (1);
		fast = fast->next;
		slow = slow->next;
	}
	return (0);
}
