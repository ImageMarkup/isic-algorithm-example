# Can be any image, including ones that depend on nvidia-docker
FROM python:3.7-slim-stretch

ADD algorithm.py /algorithm.py

CMD ["python", "algorithm.py"]
