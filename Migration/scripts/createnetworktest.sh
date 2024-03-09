sudo docker network create tnet
sudo docker run --name twebserver_v2 -v /home/ubuntu/mydev:/mydev -p 80:80 -d amitsinghbal27/topic-match-server
sudo docker run  --name tmysql -e MYSQL_DATABASE=topicmatchdb  -e MYSQL_USER=mysqluser -e MYSQL_ROOT_PASSWORD=password  -d -p 3306:33 mysql
sudo docker network connect tnet twebserver
sudo docker network connect tnet tmysql 

# pip install mysql-connector-python
