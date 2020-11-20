# ipinfo

#### 介绍


使用django 模仿cip.cc功能 练手之作


#### 软件架构
软件架构说明

```shell
#django版本
pip install django==1.11.18

# 依赖
pip install ipip-ipdb

#运行方式
python manage.py runserver 0.0.0.0:8080
```

### docker运行
```shell
# 构建
docker build -t ipinfo-django .
# 运行
docker run -d --name ipinfo -p 127.0.0.1:8080:8000 --restart=always ipinfo-django

```
### nginx配置
```shell
    location / {

        proxy_pass  http://127.0.0.1:8080/;
          #以下是一些反向代理的配置可删除.
          proxy_redirect off;
          proxy_set_header Host $host;
          #这个$host  可以是自己定义的字符串
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         #后端的Web服务器可以通过X-Forwarded-For获取用户真实IP
          client_max_body_size 10m;    
          #允许客户端请求的最大单文件字节数

          client_body_buffer_size 128k;  
          #缓冲区代理缓冲用户端请求的最大字节数，

          proxy_connect_timeout 90;  
          #nginx跟后端服务器连接超时时间(代理连接超时)

          proxy_send_timeout 90;        
          #后端服务器数据回传时间(代理发送超时)

          proxy_read_timeout 90;         
          #连接成功后，后端服务器响应时间(代理接收超时)

          proxy_buffer_size 4k;             
          #设置代理服务器（nginx）保存用户头信息的缓冲区大小
          proxy_buffers 4 32k;               
          #proxy_buffers缓冲区，网页平均在32k以下的话，这样设置
          proxy_busy_buffers_size 64k;    
          #高负荷下缓冲大小（proxy_buffers*2）
          proxy_temp_file_write_size 64k;  
          #设定缓存文件夹大小，大于这个值，将从upstream服务器传
    }

```



