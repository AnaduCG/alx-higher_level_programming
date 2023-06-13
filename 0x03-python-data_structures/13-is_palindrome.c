#include "lists.h"
/**
 *is_palindrome - function that checks if a singly linked list is a palindrome.
 *@head: pointer to the first list node
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow->next = prev;
		prev = slow;
		slow = slow->next;
	}
	if (fast != NULL)
		slow = slow->next;
	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}
	return (1);
}
