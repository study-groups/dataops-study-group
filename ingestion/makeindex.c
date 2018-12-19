#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#define BUFLEN 2048

struct index {
   uint64_t id;
   uint64_t startLine;
   uint64_t endLine;
   uint64_t numLines;
   uint64_t startByte;
   uint64_t numBytes;
};

const char* getfield(char* line, int num)
{
    const char* tok;
    for (tok = strtok(line, ",");
            tok && *tok;
            tok = strtok(NULL, ",\n"))
    {
        if (!--num)
            return tok;
    }
    return NULL;
}
int main(int argc, char **argv, char **env)
{
    FILE* fp = fopen("./test_set.csv", "r");
    char line[BUFLEN];
    uint64_t numObjToGet = 450*1000000;
    uint64_t id=0;
    uint64_t objectCount=0;
    uint64_t lineCount=0;
    uint64_t byteCount=0;
    uint64_t lineLen=0;
    struct index cur={};          /* zero out structs */

    cur.startLine = 0;
    fgets(line, BUFLEN, fp);     /* read first line with column labels */
    lineCount=1;
    byteCount = byteCount + strlen(line);
    cur.id = 0;
    cur.startByte = 0;
    cur.numBytes=byteCount;
    printf("%s",line);
      
    while (fgets(line, BUFLEN, fp) && objectCount < numObjToGet )
    {   
        lineLen =  strlen(line); 
        id = atoi(getfield(line,1));
        if(id != cur.id){  /* id has changed, note it. */
            printf("%lu,%lu,%lu,%lu,%lu\n",
                cur.id,cur.startLine, cur.numLines, 
                cur.startByte,cur.numBytes);
            objectCount++;
            cur.id = id; 
            cur.startByte = byteCount; /* byte count before adding this line */
            cur.startLine = lineCount; /* line count before adding this line */
            cur.numBytes = lineLen; 
            cur.numLines = 1; 
        }
        else {
            cur.numBytes= cur.numBytes + lineLen;
            cur.numLines= cur.numLines + 1;
        }
        byteCount = byteCount + lineLen;
        lineCount = lineCount + 1;
    }
}
