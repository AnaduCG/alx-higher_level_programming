#include "hash_tables.h"
/**
 *hash_djb2 - function that calculates the hash value of a string key
 *@str: key to a hash node
 *Return: returns a string key hash value
 *
 */
unsigned long int hash_djb2(const unsigned char *str)
{
	unsigned long int hash = 0;
	int c = 0;

	hash = 5381;
	while ((c = *str++))
	{
		hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
	}
	return (hash);
}
