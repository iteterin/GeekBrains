1. **Ядро операционной системы – это …** 
   *d. Основной компонент операционной системы, предоставляющий интерфейс системных вызовов для прикладных программ, осуществляющий управление ресурсами, выполняемыми программами*

2. ***Монолитное ядро – …** 

   *c. Все драйверы выполняются в режиме ядра, используют одно адресное пространство и прямой доступ к ресурсам, за счёт чего обеспечивается максимальное быстродействие. Требует перекомпиляции ядра при добавлении драйвера или использования механизма модульного ядра* 

3. **Когда возникает крах системы (kernel panic в Linux, BSOD в Windows NT) ?** 
   *Когда происходит сбой на уровне ядра, который система не может устранить из за перезагрузки системы (например, сбой драйвера дисковой системы, PCI или аппаратная неисправность ОЗУ)*

4. **Какие предпосылки использования ОС?** 

   1. *Разнообразие архитектур, которые не совместимы между собой* 

   2. *Приложения писались на уровне HW*, *которые не работали на другом железе*

   3. *Появилась возможность апгрейдить железо*

      *По мере роста объема софта для компьютеров, появилось необходимость использовать этот софт на разных машинах, для чего стала необходимость в какой-то стандартизации подхода исполнения и написания этих программ, или появилась необходимость в совместимости написанных программ с разным железом.* 

5.  **00 66 FF FF FF 7E 3C 18**

   *00 = 00000000; 66 = 01010101; FF = 11111111; FF = 11111111; FF = 11111111; 7E = 01111110; 3C = 00111100; 18 = 00011000*

   ░░░░░░░░░░░░░░░░
   ░░████░░░░████░░
   ████████████████
   ████████████████
   ████████████████ 
   ░░████████████░░ 
   ░░░░████████░░░░
   ░░░░░░████░░░░░░

