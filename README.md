# isic-algorithm-example
This is a template which illustrates how to package an algorithm with Docker for submission to the [ISIC Challenge](https://challenge.isic-archive.com).

# Packaging your algorithm
To package an algorithm for the ISIC Challenge, a Docker image must be created. The algorithm must meet 2 requirements:
1) The algorithm must produce scores for all JPEG images accessible at `/images`.
2) The algorithm must produce headers and scores in CSV format directly to `stdout`.   
   See below to view the output of this container when run on a set of sample images.

Once these are fulfilled, a Docker image can be built with a command like the following:
```
docker build --tag my-algorithm .
```

## Publishing your algorithm
For the ISIC Challenge to have access to your algorithm, the Docker image must be published on [Docker Hub](https://hub.docker.com/). Follow these steps to publishing:

1) [Create an account on Docker Hub](https://hub.docker.com/signup)
2) [Create a repository](https://docs.docker.com/docker-hub/repos/#creating-repositories)
3) [Push the image](https://docs.docker.com/docker-hub/repos/#pushing-a-docker-container-image-to-docker-hub)

# Running this example

## Building it locally
```
git clone git@github.com:ImageMarkup/isic-algorithm-example.git
cd isic-algorithm-example

# Note: nvidia-docker can be used when packaging your algorithms,
# but is unnecessary for this example
docker build --tag isic-algorithm-example .
docker run --volume /some/path/to/images:/images isic-algorithm-example
```

Produces:
```
image,MEL,NV,BCC,AKIEC,BKL,DF,VASC
ISIC_0001123.jpg,0.5723914558616224,0.7463878619687879,0.8076234232128179,0.9231897707170799,0.19332526246835713,0.6482625474437913,0.15089641515561825
ISIC_0001144.jpg,0.11825691475790101,0.04267257654105516,0.9684305100247566,0.5872927315239898,0.916092863517633,0.8093387127031818,0.23901828955860294
ISIC_0001121.jpg,0.05252914296507549,0.3436226223051383,0.8350598659947699,0.6641733252475985,0.506131598640143,0.23904223621096332,0.029747905783066964
ISIC_0001112.jpg,0.8791070854374194,0.7577864003676547,0.15820430519230155,0.7691369933394947,0.38171398898367126,0.6782697508415045,0.5438979497335694
ISIC_0001156.jpg,0.6405787221262385,0.618981252236539,0.554380909951646,0.24622928048692738,0.05864024517411004,0.4182158634364418,0.12481935465595972
ISIC_0001129.jpg,0.6313536294877942,0.9303769048270896,0.324156698890111,0.1412956056588851,0.8747978029983834,0.2034852808188491,0.6023688541065931
ISIC_0001155.jpg,0.767899955403678,0.8620733597021235,0.0838322530224217,0.677749802934998,0.3440302879904641,0.5858395957413736,0.4598156767085809
ISIC_0001126.jpg,0.7193682803763685,0.51738767599738,0.5370960830892982,0.820354119435515,0.11368069924405255,0.16482442856595914,0.11161550258075326
ISIC_0001136.jpg,0.7861215874743912,0.709696588380976,0.9427448381259662,0.47747312899591887,0.5966392680901971,0.14583818153128325,0.9889449714714877
ISIC_0001151.jpg,0.8497366201438511,0.7860250064139794,0.744508049352844,0.5067590276701325,0.10153519383676579,0.43614805105497934,0.643291875324321
```

## Running from Docker Hub
```
docker run --volume /some/path/to/images:/images isic/isic-algorithm-example
```
