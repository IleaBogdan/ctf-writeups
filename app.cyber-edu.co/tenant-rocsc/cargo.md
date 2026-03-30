# cargo

After doing a dirsearch on the url we fint an endpoint with code 200 named `/editor`.
When I accesed it I was hit with a big textbox and some text telling me: `Write your code here`.
After looking in the page source we can see a comment:
`<!-- Rust is cool btw-->`

Pairing it with then name of the ctf (cargo == Rust's build system and package manager) we can try writing some rust code in the box.
```rust
fn main(){
   println!("hello");
}
```

It worked.
So we know now that the box takes in rust code.

After multiple inputs trying to execute commands I finally was able to do a ls on the root dir and got this as an output:
```
Output: '/root /dev /srv /boot /usr /lib /sys /lib64 /var /run /bin /home /tmp /opt /mnt /sbin /media /proc /etc /flag39283761 '; 
```

So we can see there is a file named `/flag39283761` that probably has the flag in it.

Ok it lookis like `/flag39283761` is a directory, but it has a file named `flag2781263` in it.
So we can execute te read file function on this file (path from root): `/flag39283761/flag2781263`

![rust-exploit.rs](cargo-exploit.rs)

flag: `CTF{c7d604ecd0da6804f45d958b4c5fb622488250bd05c29b99d0134f3bfdda2fc4}`