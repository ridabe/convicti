FROM python 3.10
COPY . .
EXPOSE 5000
RUN pi install -r requirements.txt
ENTRYPOINT ["python", "main.py"]
