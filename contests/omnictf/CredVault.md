# CredVault
## Reverse Engineering (rev)

I looked in **IDA** at the binary and saw something that looked like a 5-step binder-style handshake.  
I reversed the protocol and made a script to solve it.  
Solve:
```python
#!/usr/bin/env python3
import socket
import struct
import sys


def p32(x: int) -> bytes:
    return struct.pack("<I", x & 0xFFFFFFFF)


def send_msg(sock: socket.socket, code: int, data: bytes = b"") -> None:
    sock.sendall(p32(code) + p32(len(data)) + data)


def recv_msg(sock: socket.socket):
    hdr = b""
    while len(hdr) < 8:
        chunk = sock.recv(8 - len(hdr))
        if not chunk:
            raise EOFError("connection closed while reading header")
        hdr += chunk
    code, length = struct.unpack("<II", hdr)
    body = b""
    while len(body) < length:
        chunk = sock.recv(length - len(body))
        if not chunk:
            raise EOFError("connection closed while reading body")
        body += chunk
    return code, body


def main() -> None:
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 9999
    token = 0xCA110042
    parcel = struct.pack(
        "<IIIIII",
        0xCA110001,
        token,
        1,
        0,
        0,
        token ^ 0xCA110000,
    )

    with socket.create_connection((host, port), timeout=10) as sock:
        send_msg(sock, 0xCA000002, parcel)  
        recv_msg(sock)
        send_msg(sock, 0xCA000003) 
        recv_msg(sock)
        send_msg(sock, 0xCA000004)  
        recv_msg(sock)
        send_msg(sock, 0xCA000005)  
        _, flag = recv_msg(sock)

    sys.stdout.buffer.write(flag + (b"" if flag.endswith(b"\n") else b"\n"))
    sys.stdout.buffer.flush()


if __name__ == "__main__":
    main()
```

From here I just uploaded on the ***ncat*** connection the output of this command: `base64 -w76 solve.py; echo END`

(Solved by Bogdan while Tudor was ragebaited by Codex)