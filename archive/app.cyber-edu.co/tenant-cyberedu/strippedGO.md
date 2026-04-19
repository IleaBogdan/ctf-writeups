# strippedGO

After opening the binary in ida and finding the main function (main_main from the main folder, yeah GO is a peak language) I saw this code:
```c++
v8[0] = (__int64)&RTYPE_string;
v8[1] = (__int64)&off_4DD740;
fmt_Fprintln((__int64)&go_itab__ptr_os_File_comma__ptr_io_Writer, qword_55AD10, (__int64)v8, 1, 1);
v7[0] = (__int64)&RTYPE_string;
v7[1] = (__int64)&off_4DD750;
v3 = fmt_Fprintln((__int64)&go_itab__ptr_os_File_comma__ptr_io_Writer, qword_55AD10, (__int64)v7, 1, 1);
v1 = runtime_stringtoslicebyte((__int64)v6, (__int64)"thisis32bitlongpassphraseimusing", 32);
v4 = main_EncryptAES(v1, v2, v3, (__int64)"g01sn0tf0rsk1d1e", 16);
v0 = runtime_convTstring(v4, v5);
v9[0] = (__int64)&RTYPE_string;
v9[1] = (__int64)&off_4DD760;
v10 = &RTYPE_string;
v11 = v0;
fmt_Fprintln((__int64)&go_itab__ptr_os_File_comma__ptr_io_Writer, qword_55AD10, (__int64)v9, 2, 2);
```

The main idea of this code is that it takes some strings and does an AES encryption on one of them then prints it.

The string that is encrypted was `g01sn0tf0rsk1d1e` and the key was `thisis32bitlongpassphraseimusing` (I think). So I copied the string (`g01sn0tf0rsk1d1e`) and pasted it into a sha256 online calculator and got the sha that was in the flag.

flag: `ctf{a4e394ae892144a54c008a3b480a1b22a6b64dd26c4b0c9eba498330f511b51e}`