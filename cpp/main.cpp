#include <iostream>
#include <fstream>

using namespace std;

int main() {
  cout << "I work" << endl;
  string password;
  while (true) {
    cout << "Enter the password ('rawr')" << endl;
    cin >> password;
    if (password == "rawr") {
      break;
    }
  }
}
