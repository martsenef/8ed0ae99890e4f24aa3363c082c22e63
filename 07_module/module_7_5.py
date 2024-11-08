#!/usr/bin/python3
import os
import time

directory='.'
for root, dirs, files in os.walk(directory):
	for file in files:
		filepath = os.path.join(root,file)
		tmp=os.stat(filepath)
		filetime = tmp.st_ctime
		formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
		filesize = tmp.st_size
		parent_dir = root
		print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
