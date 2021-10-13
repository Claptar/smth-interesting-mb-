#! /bin/bash
#-d fileПроверяет, существует ли файл, и является ли он директорией.
#-e fileПроверяет, существует ли файл.
#-f file Проверяет, существует ли файл, и является ли он файлом.
#-r fileПроверяет, существует ли файл, и доступен ли он для чтения.
#-s file Проверяет, существует ли файл, и не является ли он пустым.
#-w fileПроверяет, существует ли файл, и доступен ли он для записи.
#-x fileПроверяет, существует ли файл, и является ли он исполняемым.
#file1 -nt file2 Проверяет, новее ли file1, чем file2.
#file1 -ot file2Проверяет, старше ли file1, чем file2.
#-O file Проверяет, существует ли файл, и является ли его владельцем текущий пользователь.
#-G fileПроверяет, существует ли файл, и соответствует ли его идентификатор группы идентификатору группы текущего пользователя.

mydir=/home/user241/
if [ -d $mydir ]
then
  echo "The $mydir directory exists"
  cd $mydir
  ls
else
  echo "The $mydir directory does not exist"
fi
