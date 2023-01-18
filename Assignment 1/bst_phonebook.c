#include <stdio.h>
#include <stdlib.h>

/* TreeNode function to assign values as pointers necessary for further functions
   With aid of // https://stackoverflow.com/questions/33715301/inserting-nodes-in-a-binary-search-tree-c/33715699
   as many errors occured within compiler and this implementation came to be the only reasonable solution.
*/
typedef struct TreeNode {
    struct TreeNode *left;
    struct TreeNode *right;
    char *name;
    char *phone;
    char *address;
} TreeNode;

// newNode function to assign new nodes to the BST. With aid of https://www.log2base2.com/data-structures/tree/insert-a-node-in-binary-search-tree.html.
TreeNode *newNode(char *title, char *mobile, char *dir){

    TreeNode *new_node = (TreeNode *)malloc(sizeof(TreeNode));
    new_node->left = NULL;
    new_node->right = NULL;
    new_node->name = title;
    new_node->phone = mobile;
    new_node->address = dir;
    return new_node;
    
}
// Insert function to insert name into BST. With aid of https://www.log2base2.com/data-structures/tree/insert-a-node-in-binary-search-tree.html
TreeNode* insertName(TreeNode* root, char *title, char *mobile, char *dir){
    if(root == NULL)
        return newNode(title, mobile, dir);
    else if(root->name < title)
        root->right = insertName(root->right, title, mobile, dir);
    else if(root->name > title)
        root->left = insertName(root->left, title, mobile, dir);
    return root;  
}

// Find function to see if name exists within phonebook
TreeNode* findName(TreeNode *root, char *title){
    if(root == NULL) // If it does not exist
        printf("\nName has not been found\n"); // Error case if name does not exist in phonebook
    else if(root->name == title) // If found return success and contacts linked to phone number
        printf("\nName has been found\n - Phone: %s\n - Address: %s\n", root->phone, root->address);
    else if(root->name < title) // BST implementation of rules
        return findName(root->right, title);
    else if(root->name > title)
        return findName(root->right, title);
    else
        return root->name;
}
// Find function to see if phone exists within phonebook
TreeNode* findPhone(TreeNode *root, char *mobile){
    if(root == NULL) //If it does not exist
        printf("\nPhone number has not been found.\n"); // error case if phone number does not exist in phonebook
    else if(root->phone == mobile) // If found return success and contacts linked to phone number
        printf("\nPhone number has been found\n - Name: %s\n - Address: %s\n", root->name, root->address);
    else if(root->phone < mobile) //BST implementation of rules
        return findPhone(root->right, mobile);
    else if(root->phone > mobile)
        return findPhone(root->right, mobile);
    else
        return root;
}
// Function linked to remove functions in order to operate. Minimum function finds the smallest node.
TreeNode* findMinimum(TreeNode *root){
    if(root == NULL)
        return NULL;
    else if(root->right == NULL)
        return root;
    else
        return findMinimum(root->right);
}
 // Remove function for name. Implementation was supported by https://www.codesdope.com/blog/article/binary-search-tree-in-c/
TreeNode* removeName(TreeNode *root, char *title){
    if(root == NULL) // If it does not exist in phonebook display error
        printf("name does not exist within Phonebook\n");
    else if(root->name < title)
        root->right = removeName(root->right, title);
    else if(root->name > title)
        root->left = removeName(root->left, title);
    else
    {
        if(root->left == NULL && root->right == NULL)
        {
            free(root);
            return NULL;
        }
        else if(root->left == NULL || root->right == NULL)
        {
            TreeNode *temp;
            if(root->left == NULL)
                temp = root->right;
            else
                temp = root->left;
            free(root);
            return temp;
        }
        else
        {
            TreeNode *temp = findMinimum(root->right);
            root->name = temp->name;
            root->right = removeName(root->right, temp->name);
        }
    }
    return root;
}
 // Remove function for phone number. Implementation was supported by https://www.codesdope.com/blog/article/binary-search-tree-in-c/
TreeNode* removePhone(TreeNode *root, char *mobile){
    if(root == NULL) // If it does not exist in phonebook display error
        printf("Phone number does not exist within Phonebook\n");
    else if(root->phone < mobile)
        root->right = removePhone(root->right, mobile);
    else if(root->phone > mobile)
        root->left = removePhone(root->left, mobile);
    else
    {
        if(root->left == NULL && root->right == NULL)
        {
            free(root);
            return NULL;
        }
        else if(root->left == NULL || root->right == NULL)
        {
            TreeNode *temp;
            if(root->left == NULL)
                temp = root->right;
            else
                temp = root->left;
            free(root);
            return temp;
        }
        else
        {
            TreeNode *temp = findMinimum(root->right);
            root->phone = temp->phone;
            root->right = removePhone(root->right,
             temp->phone);
        }
    }
    return root;
}
// Inorder function to dislayed roots in an order of Inorder
void inorder(TreeNode *root){
    if(root == NULL) // If nothing display nothing
        return;
    inorder(root->left);
    printf(" | %s - %s - %s\n",
    root->name, 
    root->phone, 
    root->address);
    inorder(root->right);
}
// Main function where phonebook is displayed and where functions are displayed
int main(){
    TreeNode *root;

    printf("--------Welcome to the phonebook--------\nHere is a list of contacts contained within the PhoneBook:\n");

    root = insertName(root, "Leighton Adkins", "0868122244", "Dublin 11");
    root = insertName(root, "Umair Lake", "0869861452", "Dublin 24");
    root = insertName(root, "Heath Mair", "0883418472", "Dublin 4");
    root = insertName(root, "Sofia Stark", "0814672830", "Dublin 1");
    root = insertName(root, "Jean-Luc Wiggins", "0859786732", "Dublin 3");
    root = insertName(root, "Austen Daugherty", "0833336666", "Dublin 2");
    root = insertName(root, "Romario Cox", "0812345678", "Dublin 14");
    root = insertName(root, "Jolyon Sinclair", "0884628422", "Dublin 11");
    root = insertName(root, "Ajay Chamberlain", "0872548194", "Dublin 9");
    root = insertName(root, "Cathy Hood", "0874528573", "Dublin 8");
    root = insertName(root, "Lyra Herrera", "0845389502", "Dublin 6");
    root = insertName(root, "Guy Smart", "0875492641", "Dublin 2");
    root = insertName(root, "Madina Langley", "0857830909", "Dublin 11");
    root = insertName(root, "Zeshan Glover", "0864891432", "Dublin 4");
    root = insertName(root, "Janice Frye", "0854782916", "Dublin 2a");
    root = insertName(root, "Joao Pereira", "0833294067", "Portugal");
    root = insertName(root, "Cillian Damond", "0867563353", "Wexford");
    root = insertName(root, "Aisling Stokes", "0833267892", "Dublin");
    // Inorder function in operation to display phonebook in coorect seuence
    inorder(root);

    // Find function in operation for name
    printf("\nLet's see if Timmy Rodgers is in the phonebook:");
    findName(root, "");
    printf("\nLet's see if Cillian Damond is in the phonebook:");
    findName(root, "Cillian Damond");
    printf("\nLet's see if Aisling Stokes is in the phonebook:");
    findName(root, "Aisling Stokes");

    // Remove function in operation for name
    printf("\nRemove Joao from Phonebook:\n");
    root = removeName(root, "Joao Pereira");

    printf("--Here is the updated Phonebook--\n");
    inorder(root);
 
    // Find function in operation for phone
    printf("\nLet's see if 0833294067 is in the phonebook:");
    findPhone(root, "");
    printf("\nLet's see if 0869861452 is in the phonebook:");
    findPhone(root, "0869861452");
    printf("\nLet's see if 0833267892 is in the phonebook:");
    findPhone(root, "0833267892");

    // Remove function in operationfor phone numbers
    printf("\nRemove 0869861452 from Phonebook:\n");
    printf("--Here is the updated Phonebook--\n");
    root = removePhone(root, "0869861452");

    inorder(root);
    // Remove function in operation if phone number does not exist or is not within phonebook
    printf("\nRemove 050275854 from PhoneBook:\n");
    root = removePhone(root, "");
    printf("--Here is the updated Phonebook--\n");

    inorder(root);

    return 0;
}

// References
// https://www.log2base2.com/data-structures/tree/insert-a-node-in-binary-search-tree.html
// https://www.programiz.com/dsa/binary-search-tree
// https://www.codesdope.com/blog/article/binary-search-tree-in-c/
// https://stackoverflow.com/questions/27285565/c-warning-incompatible-pointer-types-passing
// https://stackoverflow.com/questions/33715301/inserting-nodes-in-a-binary-search-tree-c/33715699
