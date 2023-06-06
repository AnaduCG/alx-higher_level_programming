#include "lists.h"
/**
 *insert_node - a function that inserts a
 *		number into a sorted singly linked list
 *@head: pointer to the head of the linked list
 *@number: the numbner to be added to the list node value
 *Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = mallos(sizeof(listint_t));

	if (temp == NULL)
		return (NULL);
	temp->n = number;
	temp->next = NULL;
	if (*head == NULL)
	{
		*head = temp;
		return (temp);

	}
}
