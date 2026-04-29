# 
import hashlib
import datetime

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.transactions) + str(self.timestamp) + str(self.previous_hash)
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  

    
    def create_genesis_block(self):
        return Block(0, "Genesis Block", datetime.datetime.now(), "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        prev_block = self.get_last_block()
        new_block = Block(
            len(self.chain),
            transactions,
            datetime.datetime.now(),
            prev_block.hash
        )
        self.chain.append(new_block)
    


# Test
bc = Blockchain()
bc.add_block("A sends 10 BTC to B")
bc.add_block("B sends 20 BTC to C")
bc.add_block("C sends 30 BTC to D")

for block in bc.chain:
    print("\nBlock Index:", block.index)
    print("Transactions:", block.transactions)
    print("Timestamp:", block.timestamp)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)

# Block Index: 0
# Transactions: Genesis Block
# Timestamp: 2026-04-30 00:11:09.280158
# Previous Hash: 0
# Hash: 4571cd2b46b0fde4797a2504a1631d16fb2c52a3b7446ea96749d114040738e5

# Block Index: 1
# Transactions: A sends 10 BTC to B
# Timestamp: 2026-04-30 00:11:09.280181
# Previous Hash: 4571cd2b46b0fde4797a2504a1631d16fb2c52a3b7446ea96749d114040738e5
# Hash: 94279d3bf622f55641b3aa383c11380ce37658c5bf8e1a65e899e98b648e8d76

# Block Index: 2
# Transactions: B sends 20 BTC to C
# Timestamp: 2026-04-30 00:11:09.280187
# Previous Hash: 94279d3bf622f55641b3aa383c11380ce37658c5bf8e1a65e899e98b648e8d76
# Hash: 9a682676f821f24b26e5fa647e5c38a3ae1c94920f53c5c65e059f2fd4feac65

# Block Index: 3
# Transactions: C sends 30 BTC to D
# Timestamp: 2026-04-30 00:11:09.280190
# Previous Hash: 9a682676f821f24b26e5fa647e5c38a3ae1c94920f53c5c65e059f2fd4feac65
# Hash: 75ed40ee905aed72c74d029ac193b3b6de5a7802d8b244314eaa3c76855ca8e9