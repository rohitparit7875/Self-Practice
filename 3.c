#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

Node* create_node(int val) {
    Node *n = malloc(sizeof(Node));
    if (!n) { perror("malloc"); exit(1); }
    n->data = val;
    n->next = NULL;
    return n;
}

void insert_end(Node **head, int val) {
    Node *n = create_node(val);
    if (*head == NULL) {
        *head = n;
        return;
    }
    Node *cur = *head;
    while (cur->next) cur = cur->next;
    cur->next = n;
}

void display(Node *head) {
    printf("List: ");
    for (Node *cur = head; cur; cur = cur->next) printf("%d -> ", cur->data);
    printf("NULL\n");
}

void delete_value(Node **head, int val) {
    Node *cur = *head, *prev = NULL;
    while (cur) {
        if (cur->data == val) {
            if (prev) prev->next = cur->next;
            else *head = cur->next;
            free(cur);
            printf("Deleted %d\n", val);
            return;
        }
        prev = cur;
        cur = cur->next;
    }
    printf("%d not found in list.\n", val);
}

void free_list(Node *head) {
    while (head) {
        Node *t = head;
        head = head->next;
        free(t);
    }
}

int main() {
    Node *head = NULL;
    int choice, val;
    while (1) {
        printf("\n1: Insert  2: Display  3: Delete  4: Exit\nChoice: ");
        if (scanf("%d", &choice) != 1) break;
        if (choice == 1) {
            printf("Value to insert: ");
            scanf("%d", &val);
            insert_end(&head, val);
        } else if (choice == 2) {
            display(head);
        } else if (choice == 3) {
            printf("Value to delete: ");
            scanf("%d", &val);
            delete_value(&head, val);
        } else if (choice == 4) {
            break;
        } else {
            printf("Invalid choice.\n");
        }
    }
    free_list(head);
    return 0;
}
