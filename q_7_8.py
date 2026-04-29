import hashlib
import datetime

class Block:
    def __init__(self, index,data, previous_hash):
        self.index = index
        self.data = data
        self.timestamp = datetime.datetime.now()
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        text = str(self.index) + str(self.data) + str(self.timestamp) + str(self.previous_hash)
        return hashlib.sha256(text.encode()).hexdigest()
    
class Blockchain:
    def __init__(self):
        self.chain=[self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0,"Genesis Block", "0")
    
    def add_block(self,data):
        prev_block=self.chain[-1]
        new_block=Block(len(self.chain),data, prev_block.hash)
        self.chain.append(new_block)

    def display(self):
        for block in self.chain:
            print("\nBlock", block.index)
            print("Data:", block.data)
            print("Hash:", block.hash)
            print("Previous Hash:", block.previous_hash)

    def validate(self):
        for i in range(1,len(self.chain)):
            curr=self.chain[i]
            prev=self.chain[i - 1]

            if curr.hash != curr.calculate_hash():
                return False
            
            if curr.previous_hash != prev.hash:
                return False
        return True


blc= Blockchain()
blc.add_block("A -> B")
blc.add_block("B -> C")
blc.add_block("C -> D")
blc.add_block("D -> E")
blc.add_block("E->F")

print("\n----Blockchain--")
blc.display()

print("\n Is this blockchain valid or not ?\n","Yes" if blc.validate() else "No")

print("\n---- Tampering with Block 2---\n")
blc.chain[2].data="CORRUPTED/HACKED DATA"

#CHECKING IF IT IS VALID 
print("\nis blockchain valid after tampering or not\n","Yes" if blc.validate() else "No")