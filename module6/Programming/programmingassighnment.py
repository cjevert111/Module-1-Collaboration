from datetime import date
now = date.today()
nowfor= now.isoformat()
with open('today.txt', 'wt'):
    output.write(nowfor)

with open('today.txt', 'rt'):
    today_string = input.read()

fmt = '%Y-%m-%d\n'
datetime.strptime(today_string, fmt)

import multiprocessing

def now(seconds):
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print('wait', seconds, 'seconds, time is', datetime.utcnow())

if __name__ == '__main__':
    import random
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=now, args=(seconds,))
        proc.start()
