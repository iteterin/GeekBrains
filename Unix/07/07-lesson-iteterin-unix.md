# Введение в UNIX-системы

## Домашняя работа

### Урок 7. Практика. Запускаем веб-сервер

1. #### Установить Apache2. Прислать скриншоты работающего сервера.

   ![image-20220228223346824](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228223346824.png)

   ![image-20220228223523664](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228223523664.png)

   

2. #### \* Установить MySQL. Проверить работу, через консольного клиента, проверить команды select user from mysql.users; и select * from users;

   ![image-20220228223925048](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228223925048.png)

3. #### Установить php7.4 и phpmyadmin.

   ![image-20220228224000012](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228224000012.png)

   ![image-20220228224018959](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228224018959.png)

   ![image-20220228224713126](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228224713126.png)

   

4. #### \* Зайти пользователем root и попробовать там создать новую тестовую БД и пользователя для работы с ней. Создать в ней пару таблиц и заполнить их произвольным содержимым. Потом зайти в консольного клиента MySQL новым пользователем и вывести содержимое каждой из таблиц в новой базе данных в консоли, используя команды.

   ![image-20220228225636975](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228225636975.png)

   ![image-20220228225645949](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228225645949.png)

   ![image-20220228230045143](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228230045143.png)

   ![image-20220228230303859](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228230303859.png)

5. #### Установить Nginx и настроить его на работу с php-fpm.

           /etc/nginx/sites-enabled/default 
           <...>
           location ~ \.php$ {
                   include snippets/fastcgi-php.conf;
                   fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
           }
           <...>

   ```
   cat > cat /var/www/html/info.php << _EOL_
   <?php phpinfo(); ?>
   _EOL_
   ```

   ![image-20220228222959796](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228222959796.png)

6. #### \* Настроить Nginx в качестве балансировщика. Используя mod_upstream, раскидывать весь входящий трафик по трем Apache2-серверам, находящимся в локальной сети.

   Настройки "серверов" Apache:

   ```
   Listen 127.0.0.1:8080
   <VirtualHost 127.0.0.1:8080>
           ServerAdmin webmaster@localhost
           DocumentRoot /var/www/html
   
           ErrorLog ${APACHE_LOG_DIR}/error.log
           CustomLog ${APACHE_LOG_DIR}/access.log combined
   
   </VirtualHost> 
   ```

   Остальные выполнены по аналогии, изменен только порт и корневая директория.

   ![image-20220228222230747](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228222230747.png)

настраиваем Nginx в роли балансировщика: 

```
в фаил /etc/nginx/sites-enabled/default
добавляем: 

upstream backend{
        server 127.0.0.1:8080 weight=2;
        server 127.0.0.1:8081 weight=1;
        server 127.0.0.1:8082;
}

Следующий блок приводим к виду: 
location / {
                proxy_pass http://backend;
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Real-IP $remote_addr;
        }
```

![image-20220228222638061](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228222638061.png)

![image-20220228222709057](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228222709057.png)



