#include <stdio.h>
#include <stdbool.h>

// Function to compute the Boolean function F using logical expressions
bool compute_F(int b3, int b2, int b1, int b0) {
    // Convert bits to integer decimal minterm value
    int minterm = (b3 << 3) | (b2 << 2) | (b1 << 1) | b0;
    
    // Check if the minterm belongs to the set {0, 2, 4, 8, 10, 11, 12}
    if (minterm == 0  || minterm == 2  || minterm == 4  || 
        minterm == 8  || minterm == 10 || minterm == 11 || minterm == 12) {
        return true;
    }
    return false;
}

int main() {
    // Gray code ordering for rows (b3 b2) and columns (b1 b0)
    int gray_code[4][2] = {
        {0, 0}, // 00
        {0, 1}, // 01
        {1, 1}, // 11
        {1, 0}  // 10
    };

    printf("K-Map for F(b3, b2, b1, b0) = \\Sigma(0, 2, 4, 8, 10, 11, 12):\n\n");
    printf(" b3b2 \\ b1b0 |  00  |  01  |  11  |  10  |\n");
    printf("-----------------------------------------\n");

    // Loop through rows (b3 b2)
    for (int r = 0; r < 4; r++) {
        int b3 = gray_code[r][0];
        int b2 = gray_code[r][1];
        
        printf("    %d%d     |", b3, b2);
        
        // Loop through columns (b1 b0)
        for (int c = 0; c < 4; c++) {
            int b1 = gray_code[c][0];
            int b0 = gray_code[c][1];
            
            // Compute the output using Boolean logic evaluation
            int result = compute_F(b3, b2, b1, b0) ? 1 : 0;
            printf("  %d   |", result);
        }
        printf("\n-----------------------------------------\n");
    }

    return 0;
}

