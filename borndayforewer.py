
def check_answer(question):
  if question==1: return input('Ввведите год рождения А.С.Пушкина:')!='1799'
  if question==2: return input('В какой день июня родился Пушкин?')!='6'

while check_answer(1):print("Не верно")
while check_answer(2):print("Не верно")

print('Верно')