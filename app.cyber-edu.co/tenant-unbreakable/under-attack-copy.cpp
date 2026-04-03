#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<fcntl.h> 
#include<unistd.h>
using namespace std;

#define __int64 long long

char buffer[0x400];
int main(int argc, const char **argv, const char **envp)
{
  int flag; // [rsp+1Ch] [rbp-14h] BYREF
  int not_flag; // [rsp+20h] [rbp-10h] BYREF
  int fd; // [rsp+24h] [rbp-Ch]
  unsigned __int64 v7; // [rsp+28h] [rbp-8h]

//   v7 = __readfsqword(0x28u);
//   init();
  fd = open("/dev/urandom", 0);
  if ( fd == -1 )
  {
    puts("Open failed");
    return -1;
  }
  else if ( read(fd, &flag, 4u) == 4 )
  {
    cout<<flag<<endl;
    close(fd);
    puts("We are under attack, We need to extract the secret password from system!");
    fflush(stdout);
    while(true){
        fgets(buffer, 1024, stdin);
        printf(buffer);
    }
    printf("Please insert the password: ");
    fflush(stdout);
    scanf("%x", &not_flag);
    if ( flag == not_flag )
    {
      puts("You are the one who attack the infrastructure now!");
      system("/bin/sh");
    }
    else
    {
      puts("Permission denied!\n");
    }
    return 0;
  }
  else
  {
    puts("Read failed\n");
    return -1;
  }
}