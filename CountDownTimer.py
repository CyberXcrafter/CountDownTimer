import time

def initiate_countdown(time_remaining):
    while time_remaining:
        minutes, seconds = divmod(time_remaining, 60)
        timer_display = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer_display, end="\r")
        time.sleep(1)
        time_remaining -= 1

    print('Countdown completed!')

user_input = input('Enter the time in seconds: ')
initiate_countdown(int(user_input))
