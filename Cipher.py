# Implementing Caesar Cipher
# https://en.wikipedia.org/wiki/Caesar_cipher

class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.data)
    

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        if self.head is None:
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s
    

class CaesarCipher:
    pass
