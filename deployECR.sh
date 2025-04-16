aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 862695242185.dkr.ecr.us-east-1.amazonaws.com
docker build -t main-repo-gamer-vault-ggeasy .
docker tag main-repo-gamer-vault-ggeasy:latest 862695242185.dkr.ecr.us-east-1.amazonaws.com/main-repo-gamer-vault-ggeasy:1.0
docker push 862695242185.dkr.ecr.us-east-1.amazonaws.com/main-repo-gamer-vault-ggeasy:1.0
echo "Terminado"