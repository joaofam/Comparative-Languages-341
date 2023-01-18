data BST a = Null | Node (BST a) a (BST a) --Null is an empty tree
    deriving (Eq, Ord, Show)

search :: Ord a => BST a -> a -> Bool -- Takes a bst and a value "a", return True or False
search Null v = False --if there's an empty binary search tree and you search for a value "v", return False
search (Node treeLeft x treeRight) v --if you search a non-empty bst for a value "v", do the following:
    | x == v = True --if the current node's value "x" is equal to the value "v", return True
    | v < x = search treeLeft v -- if v is less than x, recursively search the left child
    | otherwise = search treeRight v -- if v is greater than x, recursively search the right child

insert :: Ord a => BST a -> a -> BST a --Takes a bst and a value "a", returns the bst with that value inserted
insert Null v = Node Null v Null --if tree is empty(Null), create a binary tree with the value "v" that has two empty trees as its children
insert (Node treeLeft x treeRight) v --pattern matching -if there's a left and right child then do the following:
    | x == v = Node treeLeft x treeRight --if the value "x" == value "v", then replace v with x
    | v < x = Node (insert treeLeft v) x treeRight -- if v is less than x, recursively insert the value to the left child
    | otherwise = Node treeLeft x (insert treeRight v) -- if v is greater than x, recursively insert the value to the right child

inorder :: Ord a => BST a -> [a] --Takes a bst and returns a list of the values in the bst
inorder Null = [] --If the bst is empty return an empty list
inorder (Node treeLeft v treeRight) = inorder treeLeft ++ [v] ++ inorder treeRight --otherwise if the bst is not empty, recursively go through the left child using the "++" operator to concatenate lists, followed by the root v, followed by the right child

preorder :: Ord a => BST a -> [a] --Takes a bst and returns a list of the values in the bst
preorder Null = [] --If the bst is empty return an empty list
preorder (Node treeLeft v treeRight) = [v] ++ preorder treeLeft ++ preorder treeRight --otherwise preorder traversal goes from the root to the left child and then the rightchild

postorder :: Ord a => BST a -> [a] --Takes a bst and returns a list of the values in the bst
postorder Null = [] --If the bst is empty return an empty list
postorder (Node treeLeft v treeRight) = postorder treeLeft ++ postorder treeRight ++ [v] -- otherwise traverse the left child, then the right child and lastly visit the root

--how to run code in ghci
-- :load bst.hs
--Let l = Node Null 3 Null
--l
--insert (l) 5
--insert (l) 2
--m = insert l 5 (l = letter L)