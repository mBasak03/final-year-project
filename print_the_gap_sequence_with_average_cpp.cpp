#include <bits/stdc++.h>
using namespace std;

map<char, float> hydrophobicityScale = {
    {'A', 1.80}, {'C', 2.50}, {'D', -3.50}, {'E', -3.50},
    {'F', 2.80}, {'G', -0.40}, {'H', -3.20}, {'I', 4.50},
    {'K', -3.90}, {'L', 3.80}, {'M', 1.90}, {'N', -3.50},
    {'P', -1.60}, {'Q', -3.50}, {'R', -4.50}, {'S', -0.80},
    {'T', -0.70}, {'V', 4.20}, {'W', -0.90}, {'Y', -1.30}
};

void group_by_gap_and_compute_hydrophobicity(string seq) {
    int n = seq.size();
    int gap = 1;
    while (gap <= 4) {
        cout << "gap=" << gap << ":\n";
        vector<string> groups(gap + 1);


        for (int i = 0; i < n; ++i) {
            int groupIndex = i % (gap + 1);
            groups[groupIndex] += seq[i];
        }

        for (const auto& group : groups) {
            float sum = 0.0;
            for (char c : group) {
                sum += hydrophobicityScale[c];
            }
            float avg = group.empty() ? 0.0 : sum / group.size();
            cout << group << " average=" << fixed << setprecision(2) << avg << endl;
        }
        gap++;
    }
}

int main() {
    group_by_gap_and_compute_hydrophobicity("WNPFKELERAGQRVRDAVISAAAVATVGQAAAIARG");
    return 0;
}
