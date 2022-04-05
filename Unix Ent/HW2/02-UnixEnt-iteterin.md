## Основные сервисы на Linux для предприятия

### Урок 2. Роутер на Linux, обеспечение безопасности

Домашняя работа (Тетерин Илья)

1. Собрать схему из трёх серверов. Два сервера должны иметь как минимум 3 сетевых адаптера. Один сервер должен иметь 2 сетевых адаптера. 

   ​                                  ![image-20220331040525709](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331040525709.png)

   ![image-20220331040502444](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331040502444.png)

   ![image-20220331040538926](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331040538926.png)

2. Первый интерфейс на каждой виртуальной машине имеет режим подключения bridge (сетевой мост) или nat для предоставления доступа в интернет и по ssh из родительской операционной системы. В этом примере используется bridge, так как есть роутер провайдера, который раздает IP-адреса.

   ```
   Выполнено
   ```

3. Все последующие интерфейсы между серверами организуют отдельные изолированные сегменты. Режим подключения — LAN Segment. Делается это, чтобы изолировать коммуникацию между сетевыми адаптерами устройств.

   ```
   Выполнено
   ```

4. Настроить любой из интерфейсов между server1 и server2. Назначить на него адреса из подсети 192.168.12.0/24. Второй интерфейс между ними остается отключенным и в этом задании не участвует.

   ```
   Выполнено
   ```

5. Настроить подсеть между server2 и server3 с адресами из подсети 192.168.23.0/24.

   ```
   Выполнено
   ```

6.  На каждом из серверов поднять dummy0-интерфейс и назначить на него ip-адрес 1.1.1.1/32, 2.2.2.2/32, 3.3.3.3/32 соответственно.
                                  ![image-20220331040912593](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331040912593.png)

   ![image-20220331040845072](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331040845072.png)

   ![image-20220331040929412](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331040929412.png)

7. На серверах установить пакет frr и настроить на роутерах ospf, добавив подсети 192.168.12.0/24, 192.168.23.0/24, 1.1.1.1/32, 2.2.2.2/32, 3.3.3.3/32 в area 0.
                            ![02-UnixEnt-iteterin-Server1](D:\GitRepos\GeekBrains\Unix Ent\HW2\02-UnixEnt-iteterin-Server1.jpg)

   ![02-UnixEnt-iteterin-Server2](D:\GitRepos\GeekBrains\Unix Ent\HW2\02-UnixEnt-iteterin-Server2.jpg)

   ![02-UnixEnt-iteterin-Server3](D:\GitRepos\GeekBrains\Unix Ent\HW2\02-UnixEnt-iteterin-Server3.jpg)

   

8. Убедиться, что маршрутизация работает, и с server1 вы должны пинговать 3.3.3.3 адрес на server3. Убедитесь, что нужный тип трафика разрешен в firewalld и что трафик не улетает в интернет при помощи traceroute.
   ![image-20220331044913082](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331044913082.png)

9. На server3 создайте 2 папки nfs_1 и nfs_2, добавьте их в export.

   ```bash
   yum install nfs-utils -y
   systemctl enable rpcbind nfs-server
   systemctl start rpcbind nfs-server
   mkdir /usr/nfs_1
   mkdir /usr/nfs_2
   chmod -R 777 /usr/nfs_2
   chmod -R 777 /usr/nfs_1
   cat > /etc/exports << _EOL_
   /usr/nfs_1 192.168.12.0/24(rw,sync,no_root_squash,no_all_squash)
   /usr/nfs_2 192.168.12.0/24(rw,sync,no_root_squash,no_all_squash)
   _EOL_
   exportfs -r
   firewall-cmd --permanent --zone=public --add-service=nfs
   firewall-cmd --permanent --zone=public --add-service=mountd
   firewall-cmd --permanent --zone=public --add-service=rpc-bind
   firewall-cmd --reload
   ```

10. Убедитесь, что только server1 может их примонтировать.

    ```bash
    yum install nfs-utils -y
    systemctl start rpcbind
    systemctl enable rpcbind
    mkdir /mnt/server3_nfs1
    mkdir /mnt/server3_nfs2
    mount -t nfs 192.168.23.3:/usr/nfs_1/ /mnt/server3_nfs1
    mount -t nfs 192.168.23.3:/usr/nfs_2/ /mnt/server3_nfs2
    ```

    ![image-20220331051249506](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331051249506.png)

11. Убедитесь, что после перезагрузки server1 все еще может писать и читать файлы в примонтированных папках.

    ![image-20220331052114481](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331052114481.png)

    ![image-20220331051529153](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331051529153.png)

    ![image-20220331051841539](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331051841539.png)

    ![image-20220331051908133](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331051908133.png)