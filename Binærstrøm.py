#Program som lager en strøm av binær kode
#Ofte brukt i filmer der "hacking" inngår

import random, shutil, sys, time

MIN_STRØM_LENGDE = 50
MAX_STRØM_LENGDE = 100
PAUSE = 0.1
STRØM_TEGN = ['0', '1']

TETTHET = 0.02

BREDDE = shutil.get_terminal_size()[0]

BREDDE -= 1

print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    kolonner = [0] * BREDDE
    while True:
        for i in range(BREDDE):
            if kolonner[i] == 0:
                if random.random() <= TETTHET:
                    kolonner[i] = random.randint(MIN_STRØM_LENGDE, MAX_STRØM_LENGDE)

            if kolonner[i] > 0:
                print(random.choice(STRØM_TEGN), end='')
                kolonner[i] -= 1
            else:
                print(' ', end='')

        print()
        sys.stdout.flush()
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
