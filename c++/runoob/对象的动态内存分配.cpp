#include <iostream>
using namespace std;
 
class Box
{
   public:
      Box() { 
         cout << "���ù��캯����" <<endl; 
      }
      ~Box() { 
         cout << "��������������" <<endl; 
      }
};
 
int main( )
{
   Box* myBoxArray = new Box[4];
 
   delete [] myBoxArray; // ɾ������
   return 0;
}