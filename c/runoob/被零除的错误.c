#include <stdio.h>
#include <stdlib.h>

main()
{
   int dividend = 20;
   int divisor = 0;
   int quotient;
 
   if( divisor == 0){
      fprintf(stderr, "����Ϊ 0 �˳�����...\n");
      exit(-1);
   }
   quotient = dividend / divisor;
   fprintf(stderr, "quotient ������ֵΪ : %d\n", quotient );

   exit(0);
}