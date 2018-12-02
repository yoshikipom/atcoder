#include <iostream>
#include <set>
#include <string>
using namespace std;

set<char> char_set{'a', 't', 'c', 'o', 'd', 'e', 'r', '@'};

bool check(string str1, string str2) {
  for (int i = 0; i < str1.size(); i++) {
    if (str1[i] == str2[i]) {
      continue;
    } else if (str1[i] == '@') {
      if (char_set.find(str2[i]) != char_set.end()) {
        continue;
      } else {
        return false;
      }
    } else if (str2[i] == '@') {
      if (char_set.find(str1[i]) != char_set.end()) {
        continue;
      } else {
        return false;
      }
    } else {
      return false;
    }
  }
  return true;
}

int main(int argc, char const *argv[]) {
  string str1, str2;
  bool win;
  std::cin >> str1 >> str2;

  //チェック
  win = check(str1, str2);

  if (win) {
    std::cout << "You can win" << '\n';
  } else {
    std::cout << "You will lose" << '\n';
  }
  return 0;
}
