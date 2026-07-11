# Unblur Me

After inspecting the source code of the site I saw this code:
```js
function loadSecretImage() {
    fetch('/api/v1/internal/fetch-config-blob')
    .then(response => {
        if (!response.ok) throw new Error("Failed to load");
        return response.blob();
    })
    .then(blob => {
        const blobUrl = URL.createObjectURL(blob);
        const img = document.getElementById('flag-image');
        img.src = blobUrl;
    })
    .catch(err => console.error("Error hiding image:", err));
}
```

After doing a call on the endpoint I got an image with the flag.

flag: `BRONCO{1_WOULDNT_M@K3_YOU_DO_C@LCULUS}`