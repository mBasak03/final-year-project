#include <bits/stdc++.h>
using namespace std;

map<char, float> hydrophobicityScale = {
    {'A', 1.80}, {'C', 2.50}, {'D', -3.50}, {'E', -3.50}, {'F', 2.80}, {'G', -0.40},
    {'H', -3.20}, {'I', 4.50}, {'K', -3.90}, {'L', 3.80}, {'M', 1.90}, {'N', -3.50},
    {'P', -1.60}, {'Q', -3.50}, {'R', -4.50}, {'S', -0.80}, {'T', -0.70}, {'V', 4.20},
    {'W', -0.90}, {'Y', -1.30}
};

void gapPrintWithStructural(const string& seq, const string& struct_seq) {
    int n = seq.size();

    cout << "{" << endl;
    cout << "  \"protein_sequence\": \"" << seq << "\"," << endl;
    cout << "  \"structural_sequence\": \"" << struct_seq << "\"," << endl;
    cout << "  \"sub_sequence\": [" << endl;

    for (int gap = 1; gap <= 4; ++gap) {
        cout << "    {" << endl;
        cout << "      \"gap\": " << gap << "," << endl;
        cout << "      \"sequences\": [" << endl;

        vector<string> groupSeqs(gap + 1);
        vector<string> groupStructs(gap + 1);

        for (int i = 0; i < n; ++i) {
            int idx = i % (gap + 1);
            groupSeqs[idx] += seq[i];
            groupStructs[idx] += struct_seq[i];
        }

        for (int i = 0; i <= gap; ++i) {
            string& protein_sequence = groupSeqs[i];
            string& structural_sequence = groupStructs[i];

            float sum = 0.0;
            for (char c : protein_sequence) {
                sum += hydrophobicityScale[c];
            }
            float average = protein_sequence.empty() ? 0.0f : sum / protein_sequence.size();

            cout << "        {" << endl;
            cout << "          \"protein_sequence\": \"" << protein_sequence << "\"," << endl;
            cout << "          \"average\": " << fixed << setprecision(2) << average << "," << endl;
            cout << "          \"structural_sequence\": \"" << structural_sequence << "\"" << endl;
            cout << "        }";

            if (i != gap) cout << ",";  // comma between sequences
            cout << endl;
        }

        cout << "      ]" << endl;
        cout << "    }";
        if (gap != 4) cout << ","; // comma between gap objects
        cout << endl;
    }

    cout << "  ]" << endl;
    cout << "}" << endl;
}

int main() {
    string sequence = "WNPFKELERAGQRVRDAVISAAAVATVGQAAAIARG";
    string structure = "HHHHHHHHHHHHHHHHHHHHCCCCHHHHHHHHHHHC";

    gapPrintWithStructural(sequence, structure);
    return 0;
}
