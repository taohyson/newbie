//������������ӵ��3����Ա�Ľṹ�壬�ֱ�Ϊ���͵�a���ַ��͵�b��˫���ȵ�c
//ͬʱ�������˽ṹ�����s1
//����ṹ�岢û�б������ǩ
struct 
{
    int a;
    char b;
    double c;
} s1;
 
//������������ӵ��3����Ա�Ľṹ�壬�ֱ�Ϊ���͵�a���ַ��͵�b��˫���ȵ�c
//�ṹ��ı�ǩ������ΪSIMPLE,û����������
struct SIMPLE
{
    int a;
    char b;
    double c;
};
//��SIMPLE��ǩ�Ľṹ�壬���������˱���t1��t2��t3
struct SIMPLE t1, t2[20], *t3;
 
//Ҳ������typedef����������
typedef struct
{
    int a;
    char b;
    double c; 
} Simple2;
//���ڿ�����Simple2��Ϊ���������µĽṹ�����
Simple2 u1, u2[20], *u3;

//�˽ṹ������������������Ľṹ��
struct COMPLEX
{
    char string[100];
    struct SIMPLE a;
};
 
//�˽ṹ�������������ָ���Լ����͵�ָ��
struct NODE
{
    char string[100];
    struct NODE *next_node;
};

struct B;    //�Խṹ��B���в���������
 
//�ṹ��A�а���ָ��ṹ��B��ָ��
struct A
{
    struct B *partner;
    //other members;
};
 
//�ṹ��B�а���ָ��ṹ��A��ָ�룬��A�������BҲ��֮��������
struct B
{
    struct A *partner;
    //other members;
};

#include <stdio.h>
 
struct Books
{
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
} book = {"C ����", "RUNOOB", "�������", 123456};
 
int main()
{
    printf("title : %s\nauthor: %s\nsubject: %s\nbook_id: %d\n", book.title, book.author, book.subject, book.book_id);
}