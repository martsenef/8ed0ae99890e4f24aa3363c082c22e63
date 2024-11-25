#!/usr/bin/python3

def send_email(message, recipient, sender="university.help@gmail.com"):
	domainlist=[".com",".ru",".net"]
	valid_addr=True
	for adr in [recipient,sender]:
		if not ("@" in adr and any(map(lambda d: adr.endswith(d), domainlist))):
			valid_addr=False
	if not valid_addr:
		print("Невозможно отправить письмо с адреса %s на адрес %s." %(sender,recipient))
	elif sender == recipient:
		print("Нельзя отправить письмо самому себе!")
	elif sender == "university.help@gmail.com":
		print("Письмо успешно отправлено с адреса %s на адрес%s." % (sender,recipient))
	else:
		print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса %s на адрес %s." % (sender,recipient))
	  
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
