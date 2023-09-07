#include <bits/stdc++.h>
using namespace std;

struct Interval{
    int s, e;
};

bool cmp(Interval a, Interval b){
    return a.s < b.s;
}

void insertnewinterval(vector<Interval> &intervals, Interval newinterval){
    intervals.push_back(newinterval);
    sort(intervals.begin(), intervals.end(), cmp);
    vector<Interval> res;
    res.push_back(intervals[0]);
    for(int i = 1; i<intervals.size(); i++){
        if(res.back().e >= intervals[i].s)
            res.back().e = max(res.back().e, intervals[i].e);
        else{
            res.push_back(intervals[i]);
        }
    }

    for(int i = 0; i<res.size(); i++){
        cout << res[i].s << " " << res[i].e << endl;
    }
}

int main(){
    vector<Interval> intervals;
    Interval newinterval;
}
