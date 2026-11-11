
#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 512

int main(int argc, char *argv[]) {

    FILE *file;
    char line[BUFFER_SIZE];
    char *keyword;
    int line_number = 0;
    int alert_count = 0;

    // Check command-line arguments
    if (argc != 3) {
        printf("Usage: %s <log_file> <keyword>\n", argv[0]);
        return 1;
    }

    // Get keyword from command line
    keyword = argv[2];

    // Open log file in read mode
    file = fopen(argv[1], "r");

    if (file == NULL) {
        printf("Error: Could not open file '%s'\n", argv[1]);
        return 1;
    }

    printf("====================================\n");
    printf("       LOG FILE ANALYZER\n");
    printf("====================================\n");

    printf("Log File : %s\n", argv[1]);
    printf("Keyword  : %s\n", keyword);

    printf("------------------------------------\n");
    printf("Suspicious Log Entries:\n\n");

    // Read file line by line
    while (fgets(line, sizeof(line), file) != NULL) {

        line_number++;

        // Search for keyword in current line
        if (strstr(line, keyword) != NULL) {

            alert_count++;

            printf("[ALERT] Line %d: %s",
                   line_number, line);
        }
    }

    // Display final report
    printf("\n====================================\n");
    printf("           ANALYSIS REPORT\n");
    printf("====================================\n");

    printf("Total Lines Scanned : %d\n", line_number);
    printf("Total Alerts Found  : %d\n", alert_count);

    if (alert_count == 0) {
        printf("Status: No matching entries found.\n");
    } else {
        printf("Status: Suspicious entries detected!\n");
    }

    printf("====================================\n");

    // Close the file
    fclose(file);

    return 0;
}
