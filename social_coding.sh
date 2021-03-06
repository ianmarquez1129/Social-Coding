#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp social_coding.py tempdir/.
cp location.py tempdir/.
cp tracker.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "RUN pip install requests" >> tempdir/Dockerfile
echo "COPY  ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY  ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY  social_coding.py /home/myapp/" >> tempdir/Dockerfile
echo "COPY  tracker.py /home/myapp/" >> tempdir/Dockerfile
echo "COPY  location.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/social_coding.py" >> tempdir/Dockerfile

cd tempdir

docker build -t social_codingapp .

docker run -t -d -p 5050:5050 --name social_codingrunning social_codingapp
docker ps -a
