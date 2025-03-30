
# Aqui construimos la image de la API 
```bash
docker build -t gamer-gault-lts:1.0 .
```
# Para Desarrolo local 
```bash

docker run -d -p 5000:5000 --name gamer-vault-lts-container gamer-vault-lts:1.0

```
* Nombre del contenedor **gamer-vault-lts-container**
* Imagen que contruimos **gamer-vault-lts**

# Create repository en AWS Fargate

```bash

aws ecr create-repository --repository-name  api-flask-fargate-gamer-vault 

```
#  Zero Downtime con
```bash 
docker-compose up -d --scale api=2
```

* Mantiene una instancia activa mientras la otra se reinicia.

* Cuando la nueva instancia está lista, elimina la anterior.

* Útil en entornos productivos donde no puedes permitir caída del servicio.

# install docker compose 
```bash
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

```
