#include <stdio.h>
#include <errno.h>
#include <string.h>

extern int errno ;

int main ()
{
   FILE * pf;
   int errnum;
   pf = fopen ("unexist.txt", "rb");
   if (pf == NULL)
   {
      errnum = errno;
      fprintf(stderr, "�����: %d\n", errno);
      perror("ͨ�� perror �������");
      fprintf(stderr, "���ļ�����: %s\n", strerror( errnum ));
   }
   else
   {
      fclose (pf);
   }
   return 0;
}