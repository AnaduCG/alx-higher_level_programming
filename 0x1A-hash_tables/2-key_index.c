#include "hash_tables.h"
/**
 *key_index - function that gets the index og a key un the hash
 *@key: key whose index is to be gotten
 *@size: size of the array table
 *Return:  index at which the key/value pair
 *		should be stored in the array of the hash table
 */
unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	return (hash_djb2(key) % size);
}
