#include <iostream>
#include <sstream>
#include <iomanip>
#include <openssl/sha.h>

using namespace std;

string sha256(string input) {
    unsigned char hash[SHA256_DIGEST_LENGTH];

    SHA256((unsigned char*)input.c_str(), input.size(), hash);

    stringstream ss;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        ss << hex << setw(2) << setfill('0') << (int)hash[i];
    }

    return ss.str();
}

int main() {
    string message = "Hello World";

    string result = sha256(message);

    cout << "Original Message: " << message << endl;
    cout << "SHA-256 Hash: " << result << endl;

    return 0;
}
// # Original Message is : HELLO WORLD
// # SHA-256 Hash (Encrypted): 787ec76dcafd20c1908eb0936a12f91edd105ab5cd7ecc2b1ae2032648345dff