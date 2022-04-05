## Windows Server, PowerShell и WMI

### Урок 2. Установка и настройка Windows Server

Домашнее задание:

1. Создайте нового пользователя, с необходимость смены пароля при первом входе в систему и добавьте его в группу Пользователи удаленного рабочего стола

   ![image-20220331142905194](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331142905194.png)

   ![image-20220331142844489](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331142844489.png)

2. Остановите и запустите службу SSTP (SstpSvc) из графической оболочки и из коммандной строки

   ```powershell
   Get-Service -Name SstpSvc | Stop-Service
   Get-Service -Name SstpSvc | Start-Service
   ```

   ![image-20220331143155658](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331143155658.png)

   ![image-20220331143211307](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331143211307.png)

   

3. Сожмите том, создайте раздел, потом верните в исходное состояние
                                               ![image-20220331143317617](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331143317617.png)         

   ![image-20220331143409926](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331143409926.png)

   ![image-20220331143447402](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331143447402.png)

4. Подключите второй диск, преобразуйте его в GPT
                                                            ![image-20220331144311499](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331144311499.png)

5. Добавьте третий диск, создайте из 2 и 3 диска зеркальный том
                                                           ![image-20220331144343710](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331144343710.png)
                                                          ![image-20220331144508470](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331144508470.png)

6. Найдите ИД оборудования (pci\ven например контроллер жесткого диска или видеокарта) и сайт в интернете, откуда можно скачать драйвера для этого устройства
                                                                            ![image-20220331144603868](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331144603868.png)
                                                       ![image-20220331144723346](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331144723346.png)

7. В диспетчере задач отфильтруйте приложения которые больше всего потребляют ресурсов процессора и оперативную память
                                                          ![image-20220331144847787](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331144847787.png)

   ![image-20220331144903660](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331144903660.png)

8. Отфильтруйте системные события  с кодом 6013 или 7036
   ![image-20220331145333078](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331145333078.png)

   ```powershell
   Get-EventLog -LogName System |?{$_.EventID -in 6013,7036}
   ```

9. Создайте задание, которое будет в 14.00 в рабочие дни запускать команду ping 8.8.8.8
   ![image-20220331150005571](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331150005571.png)

10. Промониторьте через Системный монтор загрузку процессора и пришлите лог
    ![image-20220331150123927](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331150123927.png)

11. Через Монитор ресурсов просмотрите в разделе Диск-Процессы с дисковой активностью-System какие используются файлы 

![image-20220331150218410](C:\Users\itete\AppData\Roaming\Typora\typora-user-images\image-20220331150218410.png)