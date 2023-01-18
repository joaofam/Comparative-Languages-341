data BinTree t = Empty | Node t (BinTree t)(BinTree t)
                 deriving (Eq, Ord, Show)

-- insert function to insert nodes
-- with aid of https://www.youtube.com/watch?v=dlHHflOEDpk & https://www.computing.dcu.ie/~davids/courses/CA320/exercise5a.hs
insert :: Ord t => t -> BinTree t -> BinTree t
insert x Empty = Node x Empty Empty
insert x (Node y left right)
    | x == y           = Node y left right
    | x < y            = Node y (insert x left) right
    | otherwise        = Node y left (insert x right)

-- search function in order to find node
-- with aid of https://www.cmi.ac.in/~spsuresh/teaching/prgh19/lectures/lecture22.pdf
-- except with switch of placement of x in line 23 to fix error
search :: Ord t => t -> BinTree t -> Bool
search x Empty = False -- if tree is empty return False as cannot search for a node
search x (Node y left right)
    | x == y                = True
    | x < y                 = search x left
    | otherwise             = search x right

-- inorder function to list nodes in inorder traversal
-- with aid of https://www.computing.dcu.ie/~davids/courses/CA320/exercise5a.hs
inorder :: BinTree t -> [t]
inorder Empty = [] -- if the bst is empty
inorder (Node x left right) = inorder left ++ [x] ++ inorder right -- produce inorder sequence of left -> root -> right

-- preorder function to list nodes in preorder traversal
preorder :: BinTree t -> [t]
preorder Empty = []
preorder (Node x left right) = [x] ++ preorder left ++ preorder right -- produce preorder sequence of root -> left -> right

-- postorder function to list nodes in postorder traversal
postorder :: BinTree t -> [t]
postorder Empty = []
postorder (Node x left right) = postorder left ++ [x] ++ postorder right -- produce postorder sequence of left -> right -> root

-- https://www.computing.dcu.ie/~davids/courses/CA320/exercise5a.hs
-- https://www.youtube.com/watch?v=a-nMwpMzZP8
-- https://stackoverflow.com/questions/21202010/implementing-binary-search-tree-insertion-in-haskell
-- https://www.cmi.ac.in/~spsuresh/teaching/prgh19/lectures/lecture22.pdcc