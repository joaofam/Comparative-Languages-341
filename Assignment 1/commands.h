#include <stdio.h>
#include <stdlib.h>
#include <string.h>



    Node *root;
    printf("--------Welcome to the phonebook--------\nHere is a list of contacts contained within the Phonebook:\n");

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

    inorder(root);

    printf("\nIf would would like to find if a name exists in the phonebook, simply enter the name you're searchin for:\n");
    char inputName;
    scanf("%s", inputName);
    findName(root, inputName)