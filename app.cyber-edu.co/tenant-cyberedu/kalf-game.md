# kalf-game

I tried to run the program, but I was hit with and error.
```
interface 'wl_output' has no event 4
thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: Os { code: 11, kind: WouldBlock, message: "Resource temporarily unavailable" }', /home/lucian/.cargo/registry/src/github.com-1ecc6299db9ec823/winit-0.19.2/src/platform/linux/wayland/event_loop.rs:126:19
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```
It was some Wayland display server issues. I fixed it with running: `export WINIT_UNIX_BACKEND=x11`

Anyways that was not part of the ctf.
If you are here to because of that issue and the lots of functions well just try running the command and then doing the ctf, beware of spoilers.

After playing the snake game a little I thought that maybe the score will give us the flag if we leak change it to some value.

After running strings on the binary I find this string: `Can you imagine that? Strings? Good. Try Harder! ctf{}\n`

Since this is rust maybe the string is put in a `println!` and in the {} is the content of the flag.
So in ida I searched for this string and found it in the function: `sub_E53C0`

Going lowwer we find: 
```c++
if ( *(_DWORD *)(a1 + 60) == 100000 )
      {
        v212 = alloc::vec::Vec$LT$T$GT$::as_slice::ha6802ce5277a5fb6(v166);
        v213 = v21;
        v144 = v212;
        v143 = v21;
        sub_BE470(v168, "eb1a4329 is the victory level!\nCan you imagine that? Strings? Good. Try Harder! ctf{}\n", 7);
        sub_BE470(v169, "9 is the victory level!\nCan you imagine that? Strings? Good. Try Harder! ctf{}\n", 1);
```
So we know we have to set the value of a1+60 to 100000.

So I looked in the assembly:
```c
loc_E59FC:
mov     rax, qword ptr [rsp+608h+var_4A0]
cmp     dword ptr [rax+3Ch], 186A0h
jz      short loc_E5A22
```

In gdb I put the breakpoint at: `0x5555554e5a04` (the binary has pie so it will differ each execution)
I then got this:
```c
pwndbg> x/10gx $rax+0x3c
0x7fffffffd774:	0x0000001e00000001	0xffff00010000001e
0x7fffffffd784:	0x0000000100007fff	0x0000000200000000
0x7fffffffd794:	0x1111111100000000	0x559a35bc3f811111
0x7fffffffd7a4:	0x0000311000005555	0xffff8c6800ff0000
0x7fffffffd7b4:	0x00000008007f2815	0x0000000000000000
```

So I setted the value of `$rax+0x3c` to 100000.
```c++
set {int}($rax+0x3c)=100000
```

flag: `ctf{ddba6614a32456631c125eb1a4327c52686c71d909a92ec05ea5eb510eae81d9}`