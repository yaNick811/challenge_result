team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 18015.2
tasks_total = 82
time_avg = 350.4
challenge_result = 'победа команды Мастера кода!'

# Использование %
print("В команде Мастера кода участников: %d !" % team1_num)
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

# Использование format()
print("Команда Волшебники данных решила задач: {} !".format(score2))
print(" Волшебники данных решили задачи за {:.1f} с !".format(team2_time))

# Использование f-строк
print(f"Команды решили {score1} и {score2} задач.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!.")