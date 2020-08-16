from nodetree import nodetree

class Tree:

    __slots__ = "root"
    """
    两个节点之间共同的parent是谁，以及两个node之间相距多少深度
    """

    def __init__(self,Val):
        self.root=nodetree(Val)

    def search(self,value,pnode,cnode):
        if pnode is None:
            return False,pnode,cnode
        else:
            if value>pnode.value:
                return self.search(value,pnode.rnode,pnode)
            if value<pnode.value:
                return self.search(value,pnode.lnode,pnode)
            else:
                return True,pnode,cnode


    def insert(self,value,pnode,cnode):
        flag,p,c=self.search(value,pnode,cnode)
        if flag is False:
            if value>c.value:
                c.rnode=nodetree(value)
            if value<c.value:
                c.lnode=nodetree(value)
        if flag is True:
            print("please do not insert the same element into the binarySearchTree")

    def delete(self,value,pnode,cnode,):
        flag,p,c=self.search(value,pnode,cnode)
        if p.lnode is None and p.rnode is None:
            if c.lnode is p:
                c.lnode=None
            if c.rnode is p:
                c.rnode=None
        elif p.lnode is None and p.rnode is not None:
            if c.lnode is p:
                c.lnode=p.rnode
            if c.rnode is p:
                c.rnode=p.rnode
        elif p.lnode is not None and p.rnode is None:
            if c.lnode is p:
                c.lnode=p.lnode
            if c.rnode is p:
                c.rnode=p.lnode
        elif p.lnode is not None and p.rnode is not None:
            pre=p.rnode
            next=pre.lnode
            while next.lnode is not None:
                pre=next
                next=next.lnode
            p.value=next.value
            pre.lnode=next.rnode





    def iteration(self,root):
        if root is not None:
            print(str(root.value)+"\t\t",end="")
            self.iteration(root.lnode)
            self.iteration(root.rnode)

    def iteration1(self, root):
        if root is not None:
            self.iteration(root.lnode)
            print(str(root.value) + "\t\t", end="")
            self.iteration(root.rnode)

    def iteration2(self, root):
        if root is not None:
            self.iteration(root.lnode)
            self.iteration(root.rnode)
            print(str(root.value) + "\t\t", end="")





def test():
    T=Tree(17)
    r=T.root
    new=nodetree(None)
    T.insert(5, r, new)
    T.insert(35, r, new)
    T.insert(2, r, new)
    T.insert(11, r, new)
    T.insert(29, r, new)
    T.insert(38, r, new)
    T.insert(9, r, new)
    T.insert(16, r, new)
    T.insert(7, r, new)
    T.insert(8, r, new)
    T.iteration(r)
    print()
    T.iteration1(r)
    print()
    T.iteration2(r)
    T.delete(5 ,r, new)
    print()
    T.iteration(r)
    # T.insert(5)
    # T.insert(2)





if __name__ == "__main__":
    test()