import schedule
import time

def tarefa():
    print('tarefa basica')

# agende a cada 5 segundo a função tarefa
schedule.every(5).seconds.do(tarefa)

while True:
    schedule.run_pending()
    time.sleep(1)