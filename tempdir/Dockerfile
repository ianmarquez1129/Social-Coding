FROM python
RUN pip install flask
RUN pip install requests
COPY  ./static /home/myapp/static/
COPY  ./templates /home/myapp/templates/
COPY  social_coding.py /home/myapp/
COPY  tracker.py /home/myapp/
COPY  location.py /home/myapp/
EXPOSE 5050
CMD python3 /home/myapp/social_coding.py
