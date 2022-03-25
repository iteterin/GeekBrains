# Введение в UNIX-системы

## Домашняя работа

### Урок 5. Сетевые возможности Linux

1. ##### Произвести ручную настройку сети в Ubuntu, на каждом шаге сделать скриншоты.

   ```bash
   mv 00-installer-config.yaml 00-installer-config.yaml.old
   cat >/etc/netplan/00-installer-config.yaml << _EOF_
   network:
     version: 2
     renderer: networkd
     ethernets:
       ens18:
         dhcp4: no
         addresses: [192.168.0.68/24]
         gateway4: 192.168.0.1
         nameservers:
           addresses:
             - 8.8.8.8
             - 8.8.4.4
   _EOF_
   
   netplan --debug generate
   netplan --debug apply && reboot now
   ```

   Импортируем конфигурацию:

   ![image-20220228151457468](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228151457468.png)

   Проверяем на ошибки:

   ![image-20220228151559709](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228151559709.png)

   Применяем:

   ![image-20220228151844749](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228151844749.png)

   ![image-20220228151936838](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228151936838.png)

2. ##### Переключить настройку сети на автоматическую через DHCP, проверить получение адреса.

   ```bash
   cat >/etc/netplan/00-installer-config.yaml << _EOF_
   network:
     version: 2
     renderer: networkd
     ethernets:
       ens18:
         dhcp4: yes
         nameservers:
           addresses:
             - 77.88.8.88
             - 77.88.8.2
   _EOF_
   
   netplan --debug generate
   netplan --debug apply && reboot now
   ```

   ![image-20220228152336240](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228152336240.png)

   ![image-20220228152501506](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228152501506.png)

   ![image-20220228152720774](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228152720774.png)

3. ##### Изменить адрес DNS на 1.1.1.1 и проверить доступность интернета, например, открыв любой браузер на адрес [https://geekbrains.ru](https://geekbrains.ru/).

   ```bash
   cat >/etc/netplan/00-installer-config.yaml<< _EOF_
   network:
     version: 2
     renderer: networkd
     ethernets:
       ens18:
         dhcp4: yes
         nameservers:
           addresses:
             - 1.1.1.1
             - 1.1.2.2
   _EOF_
   
   netplan --debug generate
   netplan --debug apply && reboot now
   ```

   ![image-20220228152849730](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228152849730.png)

   ![image-20220228153329471](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220228153329471.png)

4. ##### \* Настроить правила iptables, чтобы из внешней сети можно было обратиться только к портам 80 и 443. Запросы на порт 8080 перенаправлять на порт 80.

5. ##### \* Дополнительно к предыдущему заданию настроить доступ по ssh только из указанной сети.

6. ##### \* Настроить OpenVPN, связать несколько виртуальных машин с помощью OpenVPN-туннеля.

7. ##### \* Сделать одну из настроенных в задании выше машин шлюзом доступа в интернет. Настроить NAT.