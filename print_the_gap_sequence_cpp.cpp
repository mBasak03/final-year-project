

#include <bits/stdc++.h>
using namespace std;



void gapPrint(string seq) {
    int n = seq.size();
    int gap = 1; 
    while (gap <= 4) { 
        cout << "gap=" << gap << ":" << endl;
        vector<string> groups(gap + 1); // Create groups for each `start`
        
        for (int i = 0; i < n; ++i) {
            int groupIndex = i % (gap + 1); // Determine the group based on modulo
            groups[groupIndex] += seq[i];
        }
        
        for (const auto &group : groups) { // Print each group's characters
            cout << group << endl;
        }
        gap++;
    }
}

int main() {
    gapPrint("HHHHHHHHHHHHHHHHHHHHCCCCHHHHHHHHHHHC");
    return 0;
}
