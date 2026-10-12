#include <stdio.h>

int main() {
    // Print the header of the transition table
    printf("%-30s | %-30s\n", "Current State (Q3 Q2 Q1 Q0)", "Next State (Q3+ Q2+ Q1+ Q0+)");
    printf("-----------------------------------------------------------------\n");

    // Iterate through all 16 possible states (0 to 15)
    for (int i = 0; i < 16; i++) {
        // Extract individual bits using bitwise operations
        int q3 = (i >> 3) & 1;
        int q2 = (i >> 2) & 1;
        int q1 = (i >> 1) & 1;
        int q0 = i & 1;

        // Apply D-Flip-Flop logic based on the diagram:
        // D0 = NOT(Q3), D1 = Q0, D2 = Q1, D3 = Q2
        int next_q0 = !q3;
        int next_q1 = q0;
        int next_q2 = q1;
        int next_q3 = q2;

        // Print the current state and its corresponding next state
        printf("%-2d %-2d %-2d %-3d | %-2d %-2d %-2d %-2d\n", 
               q3, q2, q1, q0, next_q3, next_q2, next_q1, next_q0);
    }

    return 0;
}

