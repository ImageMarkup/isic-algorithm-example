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
image,MEL,NV,BCC,AK,BKL,DF,VASC,SCC,UNK
ISIC_0001112,0.5723914558616224,0.7463878619687879,0.8076234232128179,0.9231897707170799,0.19332526246835713,0.6482625474437913,0.15089641515561825,0.11825691475790101,0.04267257654105516
ISIC_0001145,0.9684305100247566,0.5872927315239898,0.916092863517633,0.8093387127031818,0.23901828955860294,0.05252914296507549,0.3436226223051383,0.8350598659947699,0.6641733252475985
ISIC_0001107,0.506131598640143,0.23904223621096332,0.029747905783066964,0.8791070854374194,0.7577864003676547,0.15820430519230155,0.7691369933394947,0.38171398898367126,0.6782697508415045
ISIC_0001102,0.5438979497335694,0.6405787221262385,0.618981252236539,0.554380909951646,0.24622928048692738,0.05864024517411004,0.4182158634364418,0.12481935465595972,0.6313536294877942
ISIC_0001142,0.9303769048270896,0.324156698890111,0.1412956056588851,0.8747978029983834,0.2034852808188491,0.6023688541065931,0.767899955403678,0.8620733597021235,0.0838322530224217
ISIC_0001101,0.677749802934998,0.3440302879904641,0.5858395957413736,0.4598156767085809,0.7193682803763685,0.51738767599738,0.5370960830892982,0.820354119435515,0.11368069924405255
ISIC_0001154,0.16482442856595914,0.11161550258075326,0.7861215874743912,0.709696588380976,0.9427448381259662,0.47747312899591887,0.5966392680901971,0.14583818153128325,0.9889449714714877
ISIC_0001129,0.8497366201438511,0.7860250064139794,0.744508049352844,0.5067590276701325,0.10153519383676579,0.43614805105497934,0.643291875324321,0.8551330034037243,0.6823995751358318
ISIC_0001116,0.8308659815752214,0.6947354561553051,0.9384569081988755,0.6666815086452151,0.5251429522147373,0.19154549910810725,0.598233910232519,0.3121559333149967,0.44596421526934504
ISIC_0001135,0.11823348315825288,0.6156315774890414,0.25647154613483825,0.8810753320645677,0.793904123694747,0.6172323147549977,0.6418036084741459,0.178078281122799,0.47220435883572487
ISIC_0001159,0.7716702127071872,0.8084827891751619,0.17309291568066731,0.22845372177455692,0.731397111128953,0.6558693749283288,0.7644535968458771,0.6627049747163055,0.6388195225615769
ISIC_0001136,0.21593893567960043,0.6086466415176203,0.8638400521130234,0.6249102297315903,0.40682913940201804,0.9101548594384917,0.8679513683706985,0.3374561424294994,0.8871672285222548
ISIC_0001140,0.4326768087505547,0.8081872017366676,0.392367827006614,0.04036497233419589,0.5629498290484529,0.06708355861243775,0.5472194467220899,0.22424345773911925,0.8548100381586853
ISIC_0001147,0.2315281038783472,0.053909984529602384,0.6226048721619478,0.7217180606769753,0.7535394456448948,0.8169864456278167,0.46641980475234257,0.4643700877899428,0.33887997232989475
ISIC_0001151,0.25769478941079826,0.5910890696446582,0.5673750252032131,0.3141896155594015,0.6834340517065248,0.3368853266638622,0.8307373090190053,0.40720399955538944,0.9955868340447789
ISIC_0001141,0.8821792729412101,0.2740329437250385,0.33829219044520287,0.083779666221388,0.5279524634617412,0.10977109918463257,0.07500854241074251,0.39219594861582363,0.3198140465761834
```

## Running from Docker Hub
```
docker run --volume /some/path/to/images:/images isic/isic-algorithm-example
```
