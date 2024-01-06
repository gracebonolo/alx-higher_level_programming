#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct list - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct list
{
	int n;
	struct list *next;
} list;


list *add_nodeint(list **head, const int n);
size_t print_listint(const list *h);
void free_listint(list *head);

#endif

