class Sql:

    def __init__(self, filepath="./data"):
        self.filepath = filepath
        self.data = dict()
        self.description = dict()

    def insert(self, table, data):
        _hash = data.__hash__()
        if not self.data.__contains__(table):
            self.data[table] = dict()
            self.description[table] = dict()
        self.data[table][_hash] = data
        for key,value in data:
            if isinstance(value,str):
                if not self.description[table].__contains__(key):
                    self.description[table][key]=Trie()
                self.description[table][key].insert(value,_hash)
            elif isinstance(value,(int,float)):
                if not self.description[table].__contains__(key):
                    self.description[table][key]=[]
                self.description[table][key][value].append(_hash)
            else:
                raise ValueError

    def update(self,table,data,filter):
        pass

    def delete(self,table,data,filter):
        pass

    def get(self,table,data,filter):
        pass





class Trie:
    class Node:
        def __init__(self):
            self.data = -1
            self.next = dict()

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, index_name: str, obj_hash):
        if index_name is None:
            return
        now = self.root
        for i in index_name:
            if not now.next.__contains__(i):
                now.next[i] = Trie.Node()
            now = now.next[i]
        now.data = obj_hash

    def filter(self, index_name: str = None, result=[], now=None):
        if now is None:
            now = self.root
            for i in index_name:
                if not now.next.__contains__(i):
                    return None
                now = now.next[i]
        if now.data is not -1:
            result.append(now.data)
        for i in now.next:
            self.filter(index_name=None, now=i, result=result)
        return result
