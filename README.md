# Botcast
Your very own take on an Owncast bot.

# Local development

## Get an Owncast instance
Run the following command to start a local container[^1]

```shell
docker run -v `pwd`/data:/app/data -p 8080:8080 -p 1935:1935 -it owncast/owncast:latest
```

# External links
- [Owncast](https://owncast.online/)
- [Build on top of Owncast](https://owncast.online/thirdparty/)

[^1]: [Owncast - Use a container image](https://owncast.online/quickstart/container/)