#include <iostream>
#include <set>
#include <string>
using namespace std;

int main(int argc, char const *argv[]) {
  string str;
  std::cin >> str;
  string result = "";
  set<char> s;
  s.insert('a');
  s.insert('i');
  s.insert('u');
  s.insert('e');
  s.insert('o');

  for (char c : str) {
    if (s.find(c) == s.end()) {
      result += c;
    }
  }
  std::cout << result << '\n';
  return 0;
}
