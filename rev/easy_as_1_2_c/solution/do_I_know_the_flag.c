#include <stdio.h>
int main()
{
   char flagLetters[16] = "-{}034abfghlnrst";
   char flag[27] = {0};

   flag[0] = flagLetters[8];
   flag[1] = flagLetters[11];
   flag[2] = flagLetters[6];
   flag[3] = flagLetters[9];
   flag[4] = flagLetters[1];
   flag[5] = flagLetters[8];
   flag[6] = flagLetters[5];
   flag[7] = flagLetters[14];
   flag[8] = flagLetters[15];
   flag[9] = flagLetters[4];
   flag[10] = flagLetters[13];
   flag[11] = flagLetters[0];
   flag[12] = flagLetters[14];
   flag[13] = flagLetters[3];
   flag[14] = flagLetters[13];
   flag[15] = flagLetters[15];
   flag[16] = flagLetters[0];
   flag[17] = flagLetters[15];
   flag[18] = flagLetters[10];
   flag[19] = flagLetters[5];
   flag[20] = flagLetters[12];
   flag[21] = flagLetters[0];
   flag[22] = flagLetters[7];
   flag[23] = flagLetters[3];
   flag[24] = flagLetters[9];
   flag[25] = flagLetters[3];
   flag[26] = flagLetters[2];

   printf("Yup, I know the flag!");
   return 0;
}