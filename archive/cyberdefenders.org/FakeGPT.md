# FakeGPT

##### Q1:
Looking inside app.js I saw this:
```javascript
const targets = [_0xabc1('d3d3LmZhY2Vib29rLmNvbQ==')];
if (targets.indexOf(window.location.hostname) !== -1) {
```
This lookes like a base64 string.

flag q1: `base64`