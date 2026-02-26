docker build -t latex-pdf-app:latest .
docker stop latex-pdf-app
docker rm latex-pdf-app
docker run -d --name latex-pdf-app -p 5000:5000 latex-pdf-app:latest
docker logs -f latex-pdf-app
