class LinkedListNode(object):
    '''
    # 链表LinkedList类的节点类
    '''
    def helpText(self):
        '''
        # LinkedListNode类的说明文档
        '''
        helpDescription = '''\033[1;32;40m--LinkedListNode类的属性列表:
        \033[1;32;40m--List:记录该节点的父链表对象
        \033[1;32;40m--Value:记录该节点储存的值
        \033[1;32;40m--Next:记录该节点在链表中的下一个节点
        \033[1;32;40m--Previous:记录该节点在链表中的上一个节点\033[0m'''
        print(helpDescription)


    def __init__(self, value):
        '''
        # 初始化链表节点类
        # value => 链表节点储存的数据
        # lis => 链表节点所属于的链表
        '''
        self.List = None
        self.Value = value
        self.Next = None
        self.Previous = None
    
    pass


class LinkedList(object):
    '''
    # 双重链接列表数据结构
    '''

    def helpText(self):
        '''
        # LinkedList类的说明文档
        '''
        helpDescription = '''
        \033[1;32;40m--LinkedList类的属性列表: 
        \033[1;32;40m       --First:记录链表的头端节点
        \033[1;32;40m       --Last:记录链表的尾端节点
        \033[1;32;40m       --Count:记录链表的节点总数

        \033[1;32;40m--LinkedList类的方法列表: 
        \033[1;32;40m       --addAfter: 向指定的链表中的节点后一位添加一个新的节点
        \033[1;32;40m       --addBefore: 向指定的链表中的节点前一位添加一个新的节点
        \033[1;32;40m       --addFirst: 向链表的头端添加数据，原先的头端数据会被向后一位移动
        \033[1;32;40m       --addLast: 向链表的末端添加数据
        \033[1;32;40m       --aggregate: 将链表中所有节点的值进行累加
        \033[1;32;40m       --allDo: 传入一个仅带有链表节点参数的方法，allDo会遍历链表中所有节点并执行传入的方法
        \033[1;32;40m       --clear: 清空链表的所有节点
        \033[1;32;40m       --contains: 检测链表所有节点中是否包含检测的值
        \033[1;32;40m       --find: 从链表中的头端开始找寻你要检索的值的节点，并且返回该节点，若没有检索到符合查找的值的节点，则返回一个空节点
        \033[1;32;40m       --findLast: 从链表中的尾端开始找寻你要检索的值的节点，并且返回该节点，若没有检索到符合查找的值的节点，则返回一个空节点
        \033[1;32;40m       --remove: 移除第一个匹配的节点
        \033[1;32;40m       --removeFirst: 移除链表的头端节点
        \033[1;32;40m       --removeLast: 移除链表的末端节点
        \033[1;32;40m       --reverse: 按照链表中节点的值排序排序节点(从大到小)
        \033[1;32;40m       --sort: 按照链表中节点的值排序排序节点(从小到大)
        \033[1;32;40m       --toArray: 返回链表转化而成的数组\033[0m
        '''
        print(helpDescription)


    def __init__(self, array = None):
        '''
        # 初始化链表
        # array => 可以不输入生成一个空链表；或者输入一个数组使其生成链表
        '''
        if array != None:
            if type(array) == list and len(array) > 0:               
                self.First = LinkedListNode(array[0])
                # self.__getList(self.First)
                temp = self.First
                temp2 = self.First
                if len(array) > 1:
                    for i in array[1:]:
                        temp.Next = LinkedListNode(i)
                        temp = temp.Next
                        # self.__getList(temp)
                        temp.Previous = temp2
                        temp2 = temp
        else:
            self.First = array
        self.allDo(self.__getList)
        self.Count = self.__checkCount()
        self.Last = self.__checkLast()

    def __checkLast(self):
        '''
        # 私有方法：检测链表末端变量Last的值
        '''
        temp = self.First
        while temp:
            if temp.Next == None:
                return temp
            temp = temp.Next

    def __checkCount(self):
        '''
        # 私有方法：检测链表长度Count的值
        '''
        count = 0
        if self.First:
            temp = self.First
            while temp:
                temp = temp.Next
                count += 1
        return count   

    def __getList(self, node):
        '''
        # 私有方法：注册链表节点，告知链表内节点它自身是在哪个链表中
        '''
        if type(node) == LinkedListNode:
            node.List = self
 
    def __removeList(self, node):
        '''
        # 私有方法：移除链表节点后注销它自身的链表
        '''
        if type(node) == LinkedListNode:
            node.List = None
    
    def __quickSort(self, arr, left, right, r):
        '''
        # 私有方法：快速排序
        # r => True：倒序排序；False：正序排序
        '''
        if left < right:
            key = arr[left]
            i = left
            j = right
            while i < j:
                if r:
                    while (i < j) and (arr[j] <= key):
                        j -= 1
                else:                   
                    while (i < j) and (arr[j] >= key):
                        j -= 1
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
                if r:
                    while (i < j) and (arr[i] >= key):
                        i += 1
                else:
                    while (i < j) and (arr[i] <= key):
                        i += 1
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
            arr[i] = key
            self.__quickSort(arr, left, i - 1, r)
            self.__quickSort(arr, j + 1, right, r)
        return arr


    def allDo(self, function):
        '''
        # 传入一个仅带有链表节点参数的方法，allDo会遍历链表中所有节点并执行传入的方法
        #  function => 传入一个仅带有链表节点参数的方法
        '''
        if self.First:
            temp = self.First
            while temp:
                function(temp)
                temp = temp.Next

    def addFirst(self, value):
        '''
        # 向链表的头端添加数据，原先的头端数据会被向后一位移动
        # value => 重载1：插入的数据； 重载2：插入一个LinkedListNode的节点
        '''
        if self.First == None:
            if type(value) == LinkedListNode:
                self.First = value
            else:
                self.First = LinkedListNode(value)
        else:                         
            temp = self.First
            if type(value) == LinkedListNode:  
                self.First = value
            else:
                self.First = LinkedListNode(value)  
            self.First.Next = temp
            temp.Previous = self.First
        self.allDo(self.__getList)
        self.Count = self.__checkCount()
        self.Last = self.__checkLast()
        pass

    def addLast(self, value):
        '''
        # 向链表的末端添加数据
        # value => 重载1：插入的数据； 重载2：插入一个LinkedListNode的节点
        '''
        if self.First == None:
            if type(value) == LinkedListNode:
                self.First = value
            else:
                self.First = LinkedListNode(value)
        else:
            temp = None
            if type(value) == LinkedListNode:
                temp = value
            else:
                temp = LinkedListNode(value)
            temp2 = self.Last
            temp2.Next = temp
            temp.Previous = temp2
        self.allDo(self.__getList)
        self.Last = self.__checkLast()
        self.Count = self.__checkCount()

        pass

    def find(self, value):
        '''
        # 从链表中的头端开始找寻你要检索的值的节点，并且返回该节点，若没有检索到符合查找的值的节点，则返回一个空节点
        # value => 检索链表中的值
        '''
        item = LinkedListNode(value)
        temp = self.First
        while temp:
            if temp.Value == item.Value:
                return temp
            temp = temp.Next
        return item

    def findLast(self, value):
        '''
        # 从链表中的尾端开始找寻你要检索的值的节点，并且返回该节点，若没有检索到符合查找的值的节点，则返回一个空节点
        # value => 检索链表中的值
        '''
        item = LinkedListNode(value)
        temp = self.Last
        while temp:
            if temp.Value == item.Value:
                return temp
            temp = temp.Previous
        return item

    def addAfter(self, node, value):
        '''
        # 向指定的链表中的节点后一位添加一个新的节点
        # node => 该链表中的节点,node参数的类型必须为LinkedListNode
        # value => 重载1：插入节点的值； 重载2：插入一个LinkedListNode的节点
        '''        
        if type(node) != LinkedListNode:
            print('node参数的类型必须为LinkedListNode')
            exit(1)
        if node.List != self:
            print('node节点不为当前链表中的节点，输入的参数node必须是当前链表中的节点')
            exit(1)
        if type(value) == LinkedListNode:
            item = value
        else:
            item = LinkedListNode(value)         
        item.Previous = node  
        item.Next = node.Next
        if node.Next:
            node.Next.Previous = item
        node.Next = item
        self.__getList(item)
        self.Count = self.__checkCount()
        self.Last = self.__checkLast()

    def addBefore(self, node, value):
        '''
        # 向指定的链表中的节点前一位添加一个新的节点
        # node => 该链表中的节点,node参数的类型必须为LinkedListNode
        # value => 重载1：插入节点的值； 重载2：插入一个LinkedListNode的节点
        '''  
        if type(node) != LinkedListNode:
            print('node参数的类型必须为LinkedListNode')
            exit(1)
        if node.List != self:
            print('node节点不为当前链表中的节点，输入的参数node必须是当前链表中的节点')
            exit(1)
        if type(value) == LinkedListNode:
            item = value
        else:
            item = LinkedListNode(value)         
        
        item.Previous = node.Previous
        if node.Previous:
            node.Previous.Next = item
        item.Next = node
        node.Previous = item
        self.__getList(item)
        self.Count = self.__checkCount()
        self.Last = self.__checkLast()

    def remove(self, value):
        '''
        # 移除第一个匹配的节点
        # value => 重载1：需要删除的值； 重载2：需要删除的链表节点
        '''
        temp = self.First
        while temp:
            if type(value) == LinkedListNode:
                if value == temp:
                    temp.Previous.Next = temp.Next
                    temp.Next.Previous = temp.Previous
                    return
            else:
                if value == temp.Value:
                    temp.Previous.Next = temp.Next
                    temp.Next.Previous = temp.Previous
                    return
            temp = temp.Next
        self.Count = self.__checkCount()
        self.Last = self.__checkLast()

    def removeFirst(self):
        '''
        # 移除链表的头端节点
        '''
        if self.First:
            temp = self.First.Next
            if temp:
                temp.Previous = None
                self.First = temp
            else:
                self.First = None
        self.Count = self.__checkCount()
        self.Last = self.__checkLast()

    def removeLast(self):
        '''
        # 移除链表的末端节点
        '''
        if self.Last:
            temp = self.Last.Previous
            if temp:
                temp.Next = None
            else:
                self.First = None
        self.Count = self.__checkCount()
        self.Last = self.__checkLast() 

    def clear(self):
        '''
        # 清空链表的所有节点
        '''
        if self.First:
            self.First = None
        self.Count = self.__checkCount()
        self.Last = self.__checkLast() 

    def sort(self):
        '''
        # 按照链表中节点的值排序排序节点(从小到大)
        '''
        arr = self.toArray()
        arr = self.__quickSort(arr, 0, (len(arr) - 1), False)
        self.clear()
        self.__init__(arr)

    def reverse(self):
        '''
        # 按照链表中节点的值排序排序节点(从大到小)
        '''
        arr = self.toArray()
        arr = self.__quickSort(arr, 0, (len(arr) - 1), True)
        self.clear()
        self.__init__(arr)

    def toArray(self):
        '''
        # 返回链表转化而成的数组
        '''
        arr = []
        temp = self.First
        while temp:
            arr.append(temp.Value)
            temp = temp.Next
        return arr

    def contains(self, value):
        '''
        # 检测链表所有节点中是否包含检测的值
        # value => 需要检测的值
        '''
        temp = self.First
        while temp:
            if temp.Value == value:
                return True
            temp = temp.Next
        return False

    def aggregate(self, Type = 0):
        '''
        # 将链表中所有节点的值进行累加
        # Tpye => 0：返回一个str类型； 1：返回一个number类型（累加将忽略非number类型）
        '''
        if Type == 0:
            txt = ''
            sign = ','
            temp = self.First
            while temp:
                s = temp.Value
                if type(s) == int:
                    s = str(s)
                txt += s
                temp = temp.Next
                if temp:
                    txt += sign
            return txt
        elif Type == 1:
            temp = self.First
            num = 0
            while temp:
                txt = temp.Value
                if type(txt) == int:
                    num += txt
                temp = temp.Next
            return num
        else:
            print('Type参数只能传入0或者1')
            exit(1)

    pass