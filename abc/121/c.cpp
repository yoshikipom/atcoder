#include <algorithm>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;
typedef long long unsigned int ll;

#define EPS (1e-7)
#define INF (1e9)
#define PI (acos(-1))
#define rep(i, n) for (int i = 0; i < n; i++)

struct Shop {
  ll price;
  ll num;
};

int main() {
  ll N, M;
  cin >> N >> M;
  vector<ll> A;
  vector<ll> B;
  vector<Shop*> shops;
  rep(i, N) {
    ll a;
    ll b;
    cin >> a >> b;
    A.push_back(a);
    B.push_back(b);
    Shop* shop = new Shop();
    shop->price = a;
    shop->num = b;
    shops.push_back(shop);
  }

  // cout << "before" << endl;
  // rep(i, N) { cout << shops[i]->price << " " << shops[i]->num << endl; }

  sort(shops.begin(), shops.end(),
       [](const Shop* a, const Shop* b) { return a->price < b->price; });

  // cout << "after" << endl;
  // rep(i, N) { cout << shops[i]->price << " " << shops[i]->num << endl; }

  ll buy = 0;
  ll wantNum = M;
  rep(i, N) {
    ll price = shops[i]->price;
    ll num = shops[i]->num;
    if (num < wantNum) {
      buy += price * num;
      wantNum -= num;
    } else {
      buy += price * wantNum;
      wantNum -= wantNum;
    }
  }

  cout << buy << endl;

  return 0;
}
