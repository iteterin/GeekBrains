1. Ознакомиться с дополнительным материалом в виде ссылок в закрепленном сообщении и методичек в материалах

   ```
   Выполнено
   ```

2. Какие процессы имеют PPID=0 ?

   ```
   root           1       0       1       1  0 дек12 ?     00:00:07 /sbin/init maybe-ubiquity
   root           2       0       0       0  0 дек12 ?     00:00:00 [kthreadd]
   ```

3. Как убить зомби?

   ```
   1. Найти PID такого процесса командой ps -xal | grep defunct (или через TOP, HTOP)
   2. Завершить командой kill -l 9 %PID% (или через HTOP) 
   ```

4. Многозадачность – это …?

   ```
   c. Возможность выполнения операционной системой нескольких задач, параллельно или последовательно, с возможностью их переключения
   ```

5. Процесс и поток – …

   ```
   c. Процесс является контейнером для потоков. Потоки, порождённые внутри процесса, используют общую память, переменные, ресурсы
   ```

6. Опишите кратко жизненный цикл процесса в OS Linux

   ```
   1. init запускает процесс bash c ID 100;
   2. пользователь в bash вводит команду ls -> происходит клонирование процесса fork(), появляется новый процесс с атрибутами PID = 200, PPID = 100. Родительский процесс переходит в состояние ожидания окончания работы дочернего - wait();
   3. Дочерний процесс (PID = 200) исполняет программу LS - exec("/bin/ls"), заменяя свой код кодом исполняемого файла;
   4. Программа ls окончив свою работу выводит в bash результат выполнения - список файлов и директорий;
   5. Дочерний процесс завершает свою работу выполнив exit(). Если по каким то приччинам дочерний процесс закончил свою работу, а родительский процесс этот сигнал не получил (или завершился раньше дочеонего), то потомок не освобождает ресурсы (хоть и не занимает процессорного времени) и переходит в состояние zombi. 
   ```

   