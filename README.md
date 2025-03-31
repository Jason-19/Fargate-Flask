
# Aqui construimos la image de la API 
```bash
docker build -t api-flask-fargate-gamer-vault .
```
# Para Desarrolo local 
```bash

docker run -d -p 5000:5000 --name gamer-vault-lts-container gamer-vault

```
* Nombre del contenedor **gamer-vault-lts-container**
* Imagen que contruimos **gamer-vault**

# Create repository en AWS Fargate

```bash
aws ecr create-repository --repository-name  api-flask-fargate-gamer-vault 
```

## Nos logueamos en AWS ECR 
Dirijete a la pestaña de ECR, ingresa al repositorio y haz clic sobre View push commands 
y copia el comando #1 en tu instancia de ec2. 
Este se encargará de hacer un login en el registry.
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 862695242185.dkr.ecr.us-east-1.amazonaws.com
```
Salida 
``Login Succeeded``

## Subir la imagen a ECR etiqueta la imagen con el tag
```bash
docker tag api-flask-fargate-gamer-vault:latest 862695242185.dkr.ecr.us-east-1.amazonaws.com/api-flask-fargate-gamer-vault:latest
docker push 862695242185.dkr.ecr.us-east-1.amazonaws.com/api-flask-fargate-gamer-vault:latest
```

##  Zero Downtime con
```bash docker-compose up -d --scale api=2```

* Mantiene una instancia activa mientras la otra se reinicia.
* Cuando la nueva instancia está lista, elimina la anterior.
* Útil en entornos productivos donde no puedes permitir caída del servicio.


# install docker compose 
```bash
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose


```
# Port Forwarding (Recomendado para RDS/Aurora)
``El comando tiene que ser todo en una sola linea``
``verificar el puerto local de mi maquina si esta ocupado (ojo)``

```bash
aws ssm start-session --target i-02ebe5b97d6f466c2 
--document-name AWS-StartPortForwardingSessionToRemoteHost 
--parameters '{"portNumber":["3306"],"host":["database-1-instance-1.c4t864a8kdls.us-east-1.rds.amazonaws.com"] ,"localPortNumber":["8400"]}' 
--region us-east-1
```
* target es el id de la instancia
* portNumber es el puerto a exponer
* host es el host de la base de datos
* localPortNumber es el puerto local de mi maquina
* region es la region de la base de datos
Si estas en windows instala el plugin para el session manager
```bash https://s3.amazonaws.com/session-manager-downloads/plugin/latest/windows/SessionManagerPluginSetup.exe ```

Salida exitosa
`` Starting session with SessionId: jnunez@bgeneral.com-gb8f8qtf92l446u7zqsc58raty ``
``Port 8400 opened for sessionId jnunez@bgeneral.com-gb8f8qtf92l446u7zqsc58raty. ``
``Waiting for connections... ``