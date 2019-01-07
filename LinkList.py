class LinkList(object):
    # 记录每个数据的对象节点
    class Node(object):
        def __init__(self, data, n = 0):
            self.data = data
            self.next = n

    def __init__(self, data = None):
        if type(data) == list:
            if len(data) > 0:
                self.head = self.Node(data[0])
                p = self.head
                if len(data) > 1:
                    for i in data[1:]:
                        node = self.Node(i)
                        p.next = node
                        p = p.next
            else:
                print('初始化不能输入空数组')
        else:
            self.head = self.Node(data)

    # 检测链表是否为空
    def isEmpty(self):
        if self.head.data == None:
            return True
        return False

    # 检测链表元素长度
    def __len__(self):
        if self.isEmpty():
            print('链表为空')
            exit(0)
        p = self.head
        _len = 0
        while p:
            _len += 1
            p = p.next
        return _len

    # 链表插值
    def insert(self, data, index):
        if index >= 0:
            if self.isEmpty():
                if index == 0:
                    self.head = self.Node(data)
                    return
                else:
                    print('超出索引界限')
                    exit(0)
            if index > len(self):
                print('超出索引界限')
                exit(0)
            if index == 0:
                p = self.head
                self.head = self.Node(data)
                self.head.next = p
                return
            p = self.head
            i = 0
            while i < index:
                parent = p
                p = p.next
                i += 1
            node = self.Node(data)
            parent.next = node
            node.next = p
        else:
            print('索引值必须大于等于0')

    # 在链表的末端添加一个数据     
    def add(self, data):
        if self.isEmpty():
            self.head = self.Node(data)
        else:
            self.insert(data,len(self))

    # 从链表头端检测返回第一个符合检索数据的索引值
    def getIndex(self, data):
        if self.isEmpty():
            print('链表为空')
            exit(1)
        index = None
        p = self.head
        i = 0
        while p:
            if p.data == data:
                index = i
                return index
            p = p.next
            i += 1
        return '没有检索到符合的数据'

    # 返回与索引值相对应的链表中的数据
    def getData(self, index):
        if index < 0:
            print('索引值不能为负数')
            exit(1)
        if self.isEmpty():
            print('链表为空')
            exit(1)
        if index > len(self) - 1:
            print('超出索引界限')
            exit(1)
        p = self.head
        i = 0
        while i < index:
            p = p.next
            i += 1
        return p.data

    # 移除链表中索引所指的数据
    def remove(self, index):
        if index < 0:
            print('索引值不能为负数')
            exit(1)
        if self.isEmpty():
            print('链表为空')
            exit(1)
        if index > len(self) - 1:
            print('超出索引界限')
            exit(1)
        p = self.head
        i = 0
        while i < index:
            par = p
            p = p.next
            i += 1
        par.next = p.next

    # 移除链表中与所指定数据一致的所有节点
    def removeAt(self, data):
        if self.isEmpty():
            print('链表为空')
            exit(1)
        
        while self.head.data == data:
            p = self.head.next
            self.head = p

        par = self.head
        p = par.next
        while p:
            if p.data == data:
                par.next = p.next
                p = par.next
            else:
                par = p
                p = par.next

    # 清空链表    
    def removeAll(self):
        if self.isEmpty():
            return
        p = self.head
        while p:
            pl = p.next
            del p
            p = pl
        self.head = self.Node(None)

    # 返回一个链表数据制成的数组
    def getArray(self):
        if self.isEmpty():
            print('链表为空')
            exit(1)
        arr = []
        p = self.head
        while p:
            arr.append(p.data)
            p = p.next
        return arr
        