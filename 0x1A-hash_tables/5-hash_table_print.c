#include "hash_tables.h"
/**
 *print_node - function that prints the values in a linked list
 *
 *@head: pointer to the first node in the list
 *
 */
void print_node(hash_node_t *head)
{
	hash_node_t *current_node = NULL;

	if (!head)
		return;
	current_node = head;
	while (current_node)
	{
		printf("'%s': '%s'", current_node->key, current_node->value);
		current_node = current_node->next;
	}
}
/**
 * hash_table_print -  function that prints a hash table.
 * @ht: hash table to be printed
 *
 */
void hash_table_print(const hash_table_t *ht)
{
	unsigned long int i = 0, count = 0;

	putchar('{');
	while (i < ht->size)
	{
		if (ht->array[i])
		{
			print_node(ht->array[i]);
			count++;
		}
		if (count > 0)
			if (ht->array[i + 1])
			{
				printf(", ");
				count = 0;
			}
		i++;
	}
	printf("}\n");
}
