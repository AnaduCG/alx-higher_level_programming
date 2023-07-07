#include "hash_tables.h"
/**
 *free_hash_nodes - function that frees a linked list
 *@head: pointer the first node in the linked list
 */
void free_hash_nodes(hash_node_t *head)
{
	hash_node_t *prev = NULL, *current = NULL;

	current = head;
	while (current)
	{
		prev = current;
		current = current->next;
		free(prev->key);
		free(prev->value);
		free(prev);
	}
	free(current);
}
/**
 * hash_table_delete - function that deletes a hash table.
 * @ht: the hash table to be freed
 */
void hash_table_delete(hash_table_t *ht)
{
	unsigned long int i = 0;

	for (; i < ht->size; i++)
	{
		free_hash_nodes(ht->array[i]);
	}
	free(ht->array);
	free(ht);
}
