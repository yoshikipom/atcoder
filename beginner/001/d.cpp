#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;

int transformTimeToNum(int time, bool isEnd) {
  int num;
  int hour = time / 100;
  int min = time % 100;
  num = (hour * 60 + min) / 5;
  if (isEnd && min % 5 != 0) {
    num += 1;
  }
  return num;
}

vector<bool> writeRainInfo(vector<bool> &vt, int start, int end) {
  int start_num = transformTimeToNum(start, false);
  int end_num = transformTimeToNum(end, true);
  // std::cout << start_num << ':' << end_num << '\n';
  for (int i = start_num; i < end_num; i++) {
    vt[i] = true;
    // std::cout << vt[i] << '\n';
  }
  return vt;
}

int transformNumToTime(int num) {
  int hour_min = num * 5;
  int hour = hour_min / 60;
  int min = hour_min % 60;
  return hour * 100 + min;
}

void output(std::vector<bool> vt) {
  for (int i = 0; i < vt.size(); i++) {
    if (vt[i] == true) {
      std::cout << std::setw(4) << std::setfill('0') << transformNumToTime(i)
                << '-';
      while (vt[i] && i <= vt.size()) {
        i++;
      }
      std::cout << std::setw(4) << std::setfill('0') << transformNumToTime(i)
                << endl;
    }
  }
}

int main(int argc, char const *argv[]) {
  vector<bool> vt(24 * 60 / 5 + 1, false);

  // input
  int num, start, end;
  std::cin >> num;
  for (size_t i = 0; i < num; i++) {
    scanf("%d-%d", &start, &end);
    // std::cout << start << '\n';
    // std::cout << end << '\n';
    writeRainInfo(vt, start, end);
  }

  output(vt);
  // for (int i = 0; i < vt.size(); i++) {
  //   std::cout << vt[i] << '\n';
  // }

  return 0;
}
