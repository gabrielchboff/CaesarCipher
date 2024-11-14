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

    def append(self, data):
        new_node = Node()
        new_node.data = data
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            base = self.head
            while base is not None and new_node.data > base.data:
                base = base.next
            if base == self.head:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif base is None:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                new_node.next = base
                new_node.prev = base.prev
                base.prev.next = new_node
                base.prev = new_node

    def pop(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            return data
        data = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        return data

    def remove(self, data):
        if self.head is None:
            return None
        base = self.head
        while base is not None and base.data != data:
            base = base.next
        if base is None:
            return None
        if base == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif base == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            base.prev.next = base.next
            base.next.prev = base.prev
        return data

    def search(self, data):
        if self.head is None:
            return None
        base = self.head
        while base is not None and base.data != data:
            base = base.next
        if base is None:
            return None
        return base

    def __len__(self):
        base = self.head
        count = 0
        while base is not None:
            count += 1
            base = base.next
        return count

    def __iter__(self):
        self.cur = self.head
        return self

    def __next__(self):
        if self.cur is None:
            raise StopIteration
        data = self.cur.data
        self.cur = self.cur.next
        return data

    def __getitem__(self, item):
        base = self.head
        for i in range(item):
            base = base.next
        return base




class CaesarCipher:
    def __init__(self, text: str = "", key: int = 0) -> None:
        self.alphabet = DoubleLinkedList()
        for i in range(26):
            self.alphabet.append(chr(ord('a') + i))
        self.alphabet.append(chr(ord('a')))
        self.alphabet.append(chr(ord('A') + 26))
        self.text = text
        self.key = key
        self.encrypted_text = ""
        self.decrypted_text = ""

    def encrypt(self):
        self.encrypted_text = ""
        for letter in self.text:
            if letter in self.alphabet:
                n = self.alphabet.search(letter)
                k = self.key
                c = (n + k) % len(self.alphabet)
                if c <= len(self.alphabet) - 1:
                    self.encrypted_text += self.alphabet[c]
                else:
                    self.encrypted_text += self.alphabet[c - len(self.alphabet)]
            else:
                self.encrypted_text += letter
        return self.encrypted_text

    def decrypt(self):
        self.decrypted_text = ""
        for letter in self.encrypted_text:
            if letter in self.alphabet:
                n = self.alphabet.search(letter)
                k = self.key
                c = (n - k) % len(self.alphabet)
                if c <= len(self.alphabet) - 1:
                    self.decrypted_text += self.alphabet[c]
                else:
                    self.decrypted_text += self.alphabet[c - len(self.alphabet)]
            else:
                self.decrypted_text += letter
        return self.decrypted_text

    def show(self):
        print(self.decrypted_text)









