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
  int not_flag; // [rsp+14h] [rbp-Ch] BYREF
  int flag; // [rsp+18h] [rbp-8h] BYREF
  int fd; // [rsp+1Ch] [rbp-4h]

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
    fflush(stdout);
    while(true){
        fgets(buffer, 1024, stdin);
        printf(buffer);
    }
    puts("Show me your ticket to pass: ");
    fflush(stdout);
    scanf("%x", &not_flag);
    if ( flag == not_flag )
      ;// restaurant();
    else
      puts("Permission denied!\n");
    return 0;
  }
  else
  {
    puts("Read failed\n");
    return -1;
  }
}