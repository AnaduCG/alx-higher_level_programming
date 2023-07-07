#include "hash_tables.h"
/**
 *linked_list_insert - function that inserts a node to a linked list
 *@head: pointer to the head node in the list
 *@key: key of the node
 *@value: the value associated with the key.
 *Return: 1 if it succeeded, 0 otherwise
 */
hash_node_t *linked_list_insert(hash_node_t **head, const char *key,
								const char *value)
{
	hash_node_t *temp = malloc(sizeof(hash_node_t));

	if (temp == NULL)
		return (NULL);

	temp->next = *head;
	temp->key = strdup(key);
	temp->value = strdup(value);

	*head = temp;
	return (temp);
}
/**
 *hash_table_set - function that adds an element to the hash table.
 *@ht: the hash table you want to add or update the key/value to
 *@key: key of the node
 *@value: the value associated with the key.
 *Return: 1 if it succeeded, 0 otherwise
 */
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	unsigned int size = 0, index = 0;
	char *key_copy;

	if (key == NULL || ht == NULL)
		return (0);

	size = ht->size;
	key_copy = strdup(key);
	if (key_copy == NULL)
		return (0);

	index = key_index((unsigned char *)key_copy, size);

	if (ht->array[index] == NULL)
	{
		ht->array[index] = linked_list_insert(&ht->array[index], key, value);
	}
	else
	{
		ht->array[index] = linked_list_insert(&(ht->array[index]), key, value);
	}

	free(key_copy);

	if (ht->array[index] == NULL)
		return (0);

	return (1);
}
