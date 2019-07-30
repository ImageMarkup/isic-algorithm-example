# isic-algorithm-example
This is a template which illustrates how to package an algorithm with Docker for submission to the [ISIC Challenge](https://challenge.isic-archive.com).

# Packaging your algorithm
To package an algorithm for the ISIC Challenge, a Docker image must be created. The algorithm must meet 2 requirements:
1) The algorithm must produce scores for all JPEG images accessible at `/images`.
2) The algorithm must produce headers and scores in CSV format directly to `stdout`.

Once these are fulfilled, a Docker image can be built with a command like the following:
```
docker build --tag my-algorithm .
```

## Publishing your algorithm
For the ISIC Challenge to have access to your algorithm, the Docker image must be published on [Docker Hub](https://hub.docker.com/).

There are a few steps to this process
1) [Create an account on Docker Hub](https://hub.docker.com/signup)
2) [Create a repository](https://docs.docker.com/docker-hub/repos/#creating-repositories)
3) [Push the image](https://docs.docker.com/docker-hub/repos/#pushing-a-docker-container-image-to-docker-hub)

# Running this example
```
git clone git@github.com:ImageMarkup/isic-algorithm-example.git
cd isic-algorithm-example

# Note: nvidia-docker can be used when packaging your algorithms,
# but is unnecessary for this example
docker build -t isic-algorithm-example .
docker run --volume $(pwd)/example-images:/images isic-algorithm-example
```
