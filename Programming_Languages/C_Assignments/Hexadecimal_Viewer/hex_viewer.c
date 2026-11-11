
#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 16

int main(int argc, char *argv[])
{
    FILE *file;
    unsigned char buffer[BUFFER_SIZE];
    size_t bytesRead;
    unsigned long offset = 0;

    // Check command-line arguments
    if (argc != 2)
    {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    // Open file in binary read mode
    file = fopen(argv[1], "rb");

    if (file == NULL)
    {
        printf("Error: Cannot open file '%s'\n", argv[1]);
        return 1;
    }

    printf("Offset      Hexadecimal Bytes                                ASCII\n");
    printf("------------------------------------------------------------------------------\n");

    // Read file 16 bytes at a time
    while ((bytesRead = fread(buffer, 1, BUFFER_SIZE, file)) > 0)
    {
        // Print offset
        printf("%08lX    ", offset);

        // Print hexadecimal values
        for (size_t i = 0; i < BUFFER_SIZE; i++)
        {
            if (i < bytesRead)
                printf("%02X ", buffer[i]);
            else
                printf("   ");
        }

        printf(" ");

        // Print ASCII representation
        for (size_t i = 0; i < bytesRead; i++)
        {
            if (buffer[i] >= 32 && buffer[i] <= 126)
                printf("%c", buffer[i]);
            else
                printf(".");
        }

        printf("\n");

        offset += bytesRead;
    }

    // Check for reading errors
    if (ferror(file))
    {
        printf("Error: Failed to read the file.\n");
        fclose(file);
        return 1;
    }

    // Close the file
    fclose(file);
    printf("\n------------------------------------------------------------------------------");
    printf("\n-> File reading completed [successfully].\n");

    return 0;
}
