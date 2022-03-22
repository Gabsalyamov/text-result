## Задача №3
В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны, пример для выполнения домашней работы можно взять [тут](https://github.com/netology-code/py-homework-basic-files/tree/master/2.4.files/sorted)  

Необходимо объединить их в один по следующим правилам:
1. Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
2. Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем

**Пример**
Даны файлы: 
1.txt
```
Строка номер 1 файла номер 1
Строка номер 2 файла номер 1
```

2.txt
```
Строка номер 1 файла номер 2
```

Итоговый файл: 
```
2.txt
1
Строка номер 1 файла номер 2
1.txt
2
Строка номер 1 файла номер 1
Строка номер 2 файла номер 1
```


## Задача №4
Для подготовки к следующей лекции прочитайте про [менеджер контекста](https://habr.com/ru/post/196382/).

---
## Как сдавать задачи
Пишите код в IDE (рекомендуем [Pycharm](https://www.jetbrains.com/ru-ru/pycharm/download/#section=windows), версия Community, инструкцию по установке вы найдете на сайте).  
- Почему лучше работать в IDE? — Ускоряет работу, есть подсветка ошибок, отладка по шагам.  
- Для более подробной информации изучите [инструкцию по работе с Pycharm](https://github.com/netology-code/guides/blob/master/python/Pycharm.md).  
- Опирайтесь на принятые [правила оформления кода](https://github.com/netology-code/codestyle/tree/master/python), чтобы выработать привычку писать профессионально. При несоблюдении принятого стиля домашние задания могут быть отправлены на доработку. 

1. Инициализируйте на своём компьютере пустой Git-репозиторий
2. Добавьте в этот же каталог необходимые файлы
3. Сделайте необходимые коммиты
4. Создайте публичный репозиторий на GitHub и свяжите свой локальный репозиторий с удалённым
5. Сделайте пуш (удостоверьтесь, что ваш код появился на GitHub)
6. Ссылку на ваш проект отправьте в личном кабинете на сайте [netology.ru](http://netology.ru/)
7. Задачи, отмеченные как необязательные, можно не сдавать, это не повлияет на получение зачета (в этом ДЗ все задачи являются обязательными)
8. Любые вопросы по решению задач задавайте в чате Slack, но мы не сможем проверить или помочь, если вы пришлете:
* архивы;
* скриншоты кода;
* теоретический рассказ о возникших проблемах.