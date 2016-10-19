#include <iostream>
#include <fstream>

using namespace std;

int main() {
  cout << "I work" << endl;
  ofstream file;
  file.open("/home/Agora/logs/cpp.log");
  file << "Yay!" << endl;
  file.close();
}
