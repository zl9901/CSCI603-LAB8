import sys
import turtle
WINDOW_WIDTH = 3000
WINDOW_HEIGHT = 3000


def init():
    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                               WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    turtle.up()
    turtle.title('Name')
    turtle.pen()
    turtle.down()
    turtle.right()
    turtle.left()

class TreeNode:
    __slots__ = 'val', "dic"

    def __init__(self, val):
        self.val = val
        self.dic =dict()

    def getStringRep(self):  # do not modify
        return self._getStringRep(0)

    def _getStringRep(self, depth):  # do not modify
        ret = self.val
        for c in self.children:
            ret += "\n" + "    " * depth + "x---" + (c._getStringRep(depth + 1))
        return ret

    def __str__(self):  # do not modify
        return str(self.val)

    def __repr__(self):  # do not modify
        return str(self.val)

    def __eq__(self, other):  # do not modify
        if type(self) != type(other):
            return False
        return self.val == other.val

class Tree:
    __slots__ = 'val', 'nodeLookup'

    def __init__(self,val):  # do not modify
        self.val = val
        self.nodeLookup = dict()

    def  addRoot(self, value):
        assert value not in self.nodeLookup and not self.root
        self.root=TreeNode(value)
        self.nodeLookup[value]=self.root

    def getNodeByValue(self, value):  # do not modify
        return self.nodeLookup[value]

    def addChildTo(self, newChildValue, parentValue):
        assert parentValue in self.nodeLookup and newChildValue not in self.nodeLookup
        cnode=TreeNode(newChildValue)
        pnode=self.getNodeByValue(parentValue)
        pnode.children.append(cnode)
        self.nodeLookup[newChildValue]=cnode




def drawPrepare():
    turtle.setx(0)
    turtle.sety(0)
    turtle.right(90)

def drawL(dic,unit):

    for keys in dic:
        if int(keys)<0:
            turtle.down()
            x = turtle.xcor()
            y = turtle.ycor()
            turtle.right(90)
            turtle.forward(abs(int(keys))*unit)
            turtle.left(90)
            turtle.forward(100)
            # turtle.done()
            if len(dic[keys]) > 1:
                drawL(dic[keys],unit/8)
            v=dic[keys]
            turtle.write(v)
            turtle.up()
            turtle.goto(x,y)


        else:
            turtle.down()
            x1 = turtle.xcor()
            y1 = turtle.ycor()
            turtle.left(90)
            turtle.forward(int(keys)*unit)
            turtle.right(90)
            turtle.forward(100)
            if len(dic[keys])>1:
                drawL(dic[keys],unit/8)
            w= dic[keys]
            turtle.write(w)
            turtle.up()
            turtle.goto(x1,y1)

def drawEnd():
    turtle.done()

def test():
    lz=Tree(0)
    # lz.addRoot(100)
    # lz.addChildTo(200,100)
    # lz.addChildTo(300, 100)
    # print(lz.nodeLookup)
    # print(lz.getNodeByValue(100))
    # print(lz.root.children)
    # lz.addChildTo(-12, 200)
    # lz.addChildTo(-3,200)
    # lz.addChildTo(15,200)
    # print(lz.getNodeByValue(200).children)
    # lz.addChildTo(7,300)
    brr=[]
    filename = sys.argv[1] + '.txt'
    with open(filename) as f:
        f.readline()
        for line in f:
            arr=line.split()
            print(arr)
            brr.append(arr)
    print()
    drr=[]
    for i in range(len(brr)-1,-1,-1):#实现字符串文本的逆序输出
        flag = True
        crr=brr[i]
        print(crr)
        for index in range(0,len(drr)):
            if crr[0]==drr[index][0]:
                flag=False
                for k in range(2, len(crr), 2):
                    try:
                        int(crr[k])
                        drr[index][1].dic[crr[k - 1]] = crr[k]
                    except:
                        print("cannot convert str to integer again")
                        hyx = TreeNode(crr[k])
                        drr.append([crr[k], hyx])
                        drr[index][1].dic[crr[k - 1]]=hyx.dic
                    #hyx=TreeNode(crr[0])
                print(lz.nodeLookup)
                print()
                print()
                print()
                # print(TreeNode(crr[0]).dic)
        if flag is True:
            for j in range(2, len(crr), 2):
                try:
                    x = int(crr[j])  # 这里不需要用到x
                    lz.nodeLookup[crr[j - 1]] = crr[j]
                except:
                    print("cannot convert str to integer")

                    hp=TreeNode(crr[j])
                    drr.append([crr[j],hp])
                    lz.nodeLookup[crr[j - 1]] =hp.dic
                print(lz.nodeLookup)
    drawPrepare()
    drawL(lz.nodeLookup,300)
    drawEnd()
    print(drr)










if __name__ == '__main__':
    test()
