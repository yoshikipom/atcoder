#include <cmath>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string transformDigToDir(double dig) {
  std::vector<string> strs{"N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                           "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"};
  int dig_int = (dig + 112.5) / 225;
  if (dig_int >= 16) {
    dig_int = 0;
  }
  return strs[dig_int];
}

int transformDisToW(double dis) {
  double dis_ps = round(dis * 10 / 60) / 10;

  if (dis_ps <= 0.2)
    return 0;
  if (dis_ps <= 1.5)
    return 1;
  if (dis_ps <= 3.3)
    return 2;
  if (dis_ps <= 5.4)
    return 3;
  if (dis_ps <= 7.9)
    return 4;
  if (dis_ps <= 10.7)
    return 5;
  if (dis_ps <= 13.8)
    return 6;
  if (dis_ps <= 17.1)
    return 7;
  if (dis_ps <= 20.7)
    return 8;
  if (dis_ps <= 24.4)
    return 9;
  if (dis_ps <= 28.4)
    return 10;
  if (dis_ps <= 32.6)
    return 11;

  return 12;
}

int main(int argc, char const *argv[]) {
  double dig, dis;
  string dir;
  int w;
  std::cin >> dig;
  std::cin >> dis;
  w = transformDisToW(dis);
  if (w != 0) {
    dir = transformDigToDir(dig);
  } else {
    dir = "C";
  }
  std::cout << dir << " " << w << '\n';
  // transformDigToDir(2750);
  // transformDisToW(628);
  return 0;
}
