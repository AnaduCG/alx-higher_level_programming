#include "hash_tables.h"
/**
 *get_node - function that gets a node in a linked list
 *@head: pointer to the first node of the linked list
 *@key: key value in the hash table
 *Return: value associated with the element, or NULL otherwise
 */
char *get_node(const hash_node_t *head, const char *key)
{
	const hash_node_t *current_node = NULL;

	if (!head)
		return (NULL);
	current_node = head;
	while (current_node)
	{
		if (strcmp(key, current_node->key) == 0)
			return (current_node->value);
		current_node = current_node->next;
	}
	return (NULL);
}
/**
 *hash_table_get - function that retrieves a value associated with a key.
 *@ht: hash table to be searched
 *@key: key value in the hash table
 *Return: value associated with the element, or NULL otherwise
 */
char *hash_table_get(const hash_table_t *ht, const char *key)
{
	unsigned char *keyy = (unsigned char *)strdup(key);
	unsigned int index = key_index(keyy, ht->size);

	free(keyy);
	return (get_node(ht->array[index], key));
}
