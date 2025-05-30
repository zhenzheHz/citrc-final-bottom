#include "testlib.h"
#include <cmath>
#include <string>
using namespace std;

const double EPS = 1e-6;

bool isNoRealRoot(const string& s) {
    return s == "no real root";
}

bool isValidDouble(const string& s) {
    char* end;
    strtod(s.c_str(), &end);
    return *end == '\0';
}

int main(int argc, char* argv[]) {
    registerTestlibCmd(argc, argv);

    string expected1 = ans.readLine();
    string actual1 = ouf.readLine();

    if (isNoRealRoot(expected1)) {
        if (!isNoRealRoot(actual1)) {
            quitf(_wa, "Expected 'no real root' but got '%s'", actual1.c_str());
        }
        quitf(_ok, "Correct: no real root");
    }
    string expected2 = ans.readLine();
    string actual2 = ouf.readLine();
    if (!isValidDouble(actual1) || !isValidDouble(actual2)) {
        quitf(_pe, "Output contains invalid float: '%s' or '%s'", actual1.c_str(), actual2.c_str());
    }
    double e1 = stod(expected1), e2 = stod(expected2);
    double a1 = stod(actual1), a2 = stod(actual2);
    bool correctOrder = fabs(a1 - e1) <= EPS && fabs(a2 - e2) <= EPS;
    bool reversedOrder = fabs(a1 - e2) <= EPS && fabs(a2 - e1) <= EPS;

    if (correctOrder || reversedOrder) {
        quitf(_ok, "Correct within error tolerance");
    }

    quitf(_wa, "Wrong output: expected (%.9f, %.9f), got (%.9f, %.9f)", e1, e2, a1, a2);
}
