# Ghost Memory

So in this ctf we have some heap allocations and we need to exploit it.
We can take a look at the `create_item` and `create_message` functions:
```c
int create_item()
{
  _QWORD *s; // [rsp+0h] [rbp-10h]
  unsigned int v2; // [rsp+Ch] [rbp-4h]

  printf("Index (0-7): ");
  v2 = read_int();
  if ( v2 >= 8 )
    return puts("Bad index");
  if ( items[v2] )
    return puts("Slot in use");
  s = malloc(72u);
  if ( !s )
  {
    puts("alloc fail");
    exit(1);
  }
  memset(s, 0, 0x48u);
  printf("Name: ");
  if ( !fgets((char *)s, 64, stdin) )
    exit(0);
  *((_BYTE *)s + strcspn((const char *)s, "\n")) = 0;
  s[8] = normal;
  items[v2] = s;
  return printf("Created item %d\n", v2);
}
int create_message()
{
  const char *v1; // rbx
  signed int v2; // [rsp+Ch] [rbp-14h]

  printf("Index (0-7): ");
  v2 = read_int();
  if ( (unsigned int)v2 >= 8 )
    return puts("Bad index");
  if ( *((_QWORD *)&messages + v2) )
    return puts("Slot in use");
  *((_QWORD *)&messages + v2) = malloc(0x48u);
  if ( !*((_QWORD *)&messages + v2) )
  {
    puts("alloc fail");
    exit(1);
  }
  printf("Message (up to %zu bytes): ", 0x47u);
  if ( !fgets(*((char **)&messages + v2), 72, stdin) )
    exit(0);
  v1 = (const char *)*((_QWORD *)&messages + v2);
  v1[strcspn(v1, "\n")] = 0;
  return printf("Created message %d\n", v2);
}
```

Both functions call malloc on 0x48 bytes and `create_item` reads only 64 bytes from us but `create_message` reads 72. The other 8 bytes from `create_item` is used in saving a function pointer that we can call via `show_item`.
By this logic we can follow a workflow like this one and get use after free:
`allocate an item` -> `delete it` -> `allocate an message and write 72 bytes in it`

The main point is to overwrite the 8 bytes that have a function pointer at the end. This will happen since the deleted item will be saved in tcachebins and the next time we malloc something of the size it is (0x48) we will get it.

The second part which enables us to use it this way is that it never checks in `show_item` if the item was freed or not. So we can overwirte it with a message item and put the address of the win function.

So we can use this exploit script to get the flag:
![exploit](Ghost_Memory_exploit.py)

flag: `T43CTF{read_it_twice}`