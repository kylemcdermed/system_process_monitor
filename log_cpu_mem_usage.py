import psutil
import time
import logging

logger = logging.getLogger('main_logger')
file_handler = logging.FileHandler('logs.out')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.WARNING)

def display_usage(cpu_usage,mem_usage,bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    mem_percent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    if cpu_percent >= 75:
        logging.warning(f'CPU Usage is at {cpu_percent:.2f}%')
    if cpu_percent >= 80:
        logging.warning(f'CPU Usage is at {cpu_percent:.2f}%')
    elif cpu_percent >= 90:
        logging.critical(f'CPU Usage is at {cpu_usage:.2f}%')
    else:
        print(f'\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}% ',end='')
        print(f'MEM Usage: |{mem_bar}| {mem_usage:.2f}% ',end='')

# Start monitoring in a loop
try:
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage over 5 second
        mem_usage = psutil.virtual_memory().percent  # Get memory usage
        display_usage(cpu_usage, mem_usage)
        
        # Sleep for 5 seconds before checking again
        time.sleep(5)

except KeyboardInterrupt:
    # Allow graceful exit with Ctrl+C
    print("\nMonitoring stopped.")

