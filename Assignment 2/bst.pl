BinTree(left, x, right).

% insert function to place a element in BST
% with aid of https://www.computing.dcu.ie/~davids/courses/CA208/CA208_Prolog_2p.pdf
insert(Empty, x, BinTree(Empty, x, Empty)).
insert(BinTree(left, Root, right), x, BinTree(new_left, Root, right)) :-
    x =< Root, insert(left, x, new_left.
insert(BinTree(left, Root, right), x, BinTree(left, Root, new_right)) :-
    x =< Root, insert(right, x, new_right).

% search function to find element
% with aid of https://www.computing.dcu.ie/~davids/courses/CA208/CA208_Prolog_2p.pdf
search(x, BinTree(left, x, right)).
search(x, BinTree(left, Root, right)) :-
    X =< Root, search(x, left).
search(x, BinTree(Root, left right)) :-
    search(x, right).

% inorder function to list nodes in inorder traversal
% in aid with https://sites.google.com/site/prologsite/prolog-problems/4/solutions-4
% produce inorder sequence of left - root - right
inorder(Empty, []).
inorder(BinTree(x, left, right), List) :-
    inorder(left, new_left),
    inorder(right, new_right),
    append(new_left, [x|new_right], List).

% preorder function to list nodes in preorder traversal
% in aid with https://sites.google.com/site/prologsite/prolog-problems/4/solutions-4
% produce preorder sequence of root - left - right
preorder(Empty, []).
preorder(BinTree(x, left, right), [x|List]) :-
    preorder(left, new_left),
    preorder(right, new_right),
    append(new_left, new_right, List).

% postorder function to list nodes in postorder traversal
% with aid of https://www.cse.iitd.ac.in/~saroj/LFP/LFP_2013/L10.pdf
% produce postorder sequence of left - right - root
postorder(Empty, []).
postorder(BinTree(x, left, right), List) :- 
    postorder(left, new_left), 
    postorder(right, new_right), 
    append(new_right, [x], newer_right), 
    append(new_left, newer_right, List).


% https://www.computing.dcu.ie/~davids/courses/CA208/CA208_Prolog_2p.pdf
% https://www.cse.iitd.ac.in/~saroj/LFP/LFP_2013/L10.pdf
% https://sites.google.com/site/prologsite/prolog-problems/4/solutions-4
