#include <iostream>
#include <vector>
#include <string>

using namespace std;

void markRepeats(const string& sequence, int threshold) {
    int n = sequence.length();
    int start = 0;

    while (start < n) {
        int end = start;
        // Expand while same character
        while (end + 1 < n && sequence[end + 1] == sequence[start]) {
            end++;
        }
        // Check if the run length meets the threshold
        if (end - start + 1 >= threshold) {
            cout << sequence[start] << ":(" << start << "-" << end << ") ";
        }
        // Move to next segment
        start = end + 1;
    }
    cout << endl;
}

int main() {
    vector<string> sequences = {
        "CCCTTTTC",
        "TTTGGGCC",
        "CCCBTTTBC",
        "CGGGTTTCCC",
        "CHHHHHCCCC"
    };

    int threshold = 3;

    for (const string& seq : sequences) {
        cout << "Sequence: " << seq << " -> ";
        markRepeats(seq, threshold);
    }

    return 0;
}
