class nodetree:

    __slots__ = "value","lnode","rnode"

    def __init__(self,value):
        self.value=value
        self.lnode=None
        self.rnode=None
