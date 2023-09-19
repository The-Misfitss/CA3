FROM python
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN make test
EXPOSE 5000
CMD python app.py