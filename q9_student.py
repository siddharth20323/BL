// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint public storedData;

    // Function to set value
    function set(uint x) public {
        storedData = x;
    }

    // Function to get value
    function get() public view returns (uint) {
        return storedData;
    }
}

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentInfo {
    
    struct Student {
        string name;
        uint age;
    }

    Student public student;

    // Function to set student details
    function setStudent(string memory _name, uint _age) public {
        student = Student(_name, _age);
    }

    // Function to get student details
    function getStudent() public view returns (string memory, uint) {
        return (student.name, student.age);
    }
}

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TransferFunds {

    // Deposit Ether into contract
    function deposit() public payable {}

    // Check contract balance
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }

    // Transfer Ether to another address
    function transfer(address payable _to, uint _amount) public {
        require(address(this).balance >= _amount, "Insufficient balance");
        _to.transfer(_amount);
    }
}