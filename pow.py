

import hashlib
import datetime

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.transactions) + str(self.timestamp) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()
    
    def mine_block(self, difficulty):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1  
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self, difficulty):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block",  datetime.datetime.now(), "0")  
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), data, datetime.datetime.now(), prev_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def display_chain(self):
        for block in self.chain:
            print("\n-------------")
            print("Index:", block.index)
            print("Transactions:", block.transactions)  
            print("Timestamp:", block.timestamp)
            print("Nonce:", block.nonce)
            print("Hash:", block.hash)
            print("Previous Hash:", block.previous_hash)



blc = Blockchain(difficulty=2)

blc.add_block("A->B")
blc.add_block("B->C")
blc.add_block("C->D")

blc.display_chain()

# Index: 0
# Transactions: Genesis Block
# Timestamp: 2026-04-30 00:09:00.401799
# Nonce: 122
# Hash: 00075a6ea69500039c25af8b6c2fddc6d671d4eb133c07cb75250a0d31a1f659
# Previous Hash: 0

# -------------
# Index: 1
# Transactions: A->B
# Timestamp: 2026-04-30 00:09:00.401985
# Nonce: 173
# Hash: 005f8098359b69e4d315cccf68d9e7b641fed45456a8c1bc6157d801447c256b
# Previous Hash: 00075a6ea69500039c25af8b6c2fddc6d671d4eb133c07cb75250a0d31a1f659

# -------------
# Index: 2
# Transactions: B->C
# Timestamp: 2026-04-30 00:09:00.402214
# Nonce: 3
# Hash: 0003626682ec59bc5f8b9969c1b00b46539903ece739e49bea8a396c77ec68ad
# Previous Hash: 005f8098359b69e4d315cccf68d9e7b641fed45456a8c1bc6157d801447c256b

# -------------
# Index: 3
# Transactions: C->D
# Timestamp: 2026-04-30 00:09:00.402220
# Nonce: 277
# Hash: 0022bf861952fb758f04ddaad953220f81af4d62806e597709919461496353df
# Previous Hash: 0003626682ec59bc5f8b9969c1b00b46539903ece739e49bea8a396c77ec68ad