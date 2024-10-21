#!/usr/bin/python3
from time import sleep

class User:
	def __init__(self,nickname,password,age):
		self.nickname=nickname
		self.password=password
		self.age=age
	def __str__(self):
		return self.nickname
class Video:
	def __init__(self,title,duration,adult_mode=False):
		self.title=title
		self.duration=duration
		self.adult_mode=adult_mode
		self.time_now=0
class UrTube:
	AdultAge=18
	def __init__(self):
		self.users={}
		self.videos={}
		self.current_user=None
	def log_in(self,nickname,password):
		self.current_user = nickname if nickname in self.users and self.users[nickname].password==hash(password) else None
	def register(self,nickname,password,age):
		if nickname in self.users:
			print("Пользователь "+nickname+" уже существует")
		else:
			u=User(nickname,hash(password),age)
			self.users[nickname]=u
			self.current_user=u
	def log_out(self):
		self.current_user=None
	def add(self,*videos):
		for v in videos:
			if not v.title in self.videos:
				self.videos[v.title]=v
	def get_videos(self,pat):
		return list(map(lambda x: x.title,filter(lambda v: pat.casefold() in v.title.casefold(),self.videos.values())))
	def watch_video(self,video):
		if(self.current_user==None):
			print("Войдите в аккаунт, чтобы смотреть видео")
			return
		if video in self.videos:
			v=self.videos[video]
			if v.adult_mode and self.current_user.age<self.AdultAge:
				print("Вам нет 18 лет, пожалуйста покиньте страницу")
				return
			for i in range (v.duration):
				v.time_now=i
				print(i,end=" ",flush=True)
				sleep(0.1)
			v.time_now=0
			print("Конец видео")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
print(ur.videos)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')			
