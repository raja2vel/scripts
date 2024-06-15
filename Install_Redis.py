#! /usr/bin/python3
# import Modules
import sys
import subprocess
import os

# Define the Functions:
# Only allow for Root Users

if os.geteuid()==0:
  print('Allowed to execute.')
else:
  print('Access denied. Execute as Sudoer.')

# Installing the redis server.

def install_redis ():

    # Update the package list
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)

    # Install Redis
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'redis-server'], check=True)

        print ("Redis Installed succefully")

def start_redis():
    try:
    # Enable and start Redis service
        subprocess.run(['sudo', 'systemctl', 'enable', 'redis-server'], check=True)
        subprocess.run(['sudo', 'systemctl', 'start', 'redis-server'], check=True)
        
        print("Redis started successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def check_redis_status():
    try:
        # Check if Redis server is running
        result = subprocess.run(['redis-cli', 'ping'])
        #if result.returncode == 0 and result.stdout.strip() == "PONG":
      #  print("Redis server is running.")
      #  else:
        #    print("Redis server is not running.")
    except subprocess.CalledProcessError as e:
        print("An error occurred while checking Redis status: {e}")

def stop_redis():
        
    # Stop the redis Service.
    try:
        subprocess.run(['sudo', 'systemctl', 'stop', 'redis-server'], check=True)
    
        print("Redis stopped successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def restart_redis():
        # Restart the redis Service.
    try:
        subprocess.run(['sudo', 'systemctl', 'restart', 'redis-server'], check=True)
    
        print("Redis restarted successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def backup_redis():
    # Issue the BGSAVE command to create a backup
    try:
        result = subprocess.run(['redis-cli', 'BGSAVE'])
        if result.returncode==0:
          print("Redis backup started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
def uninstall_redis():
    # Uninstall the redis server

    try:
        subprocess.run(['sudo', 'apt-get','purge', '--auto-remove', 'redis-server','-y'], check=True)
        print("Redis removing started successfully.")

        # Redis Data path declaration
        redis_conf_dir = '/etc/redis'
        redis_data_dir = '/var/lib/redis'

        subprocess.run(['sudo', 'rm', '-rf', redis_conf_dir], check=True)
        print(f"Redis configuration directory {redis_conf_dir} removed successfully.")

        subprocess.run(['sudo', 'rm', '-rf', redis_data_dir], check=True)
        print(f"Redis configuration directory {redis_data_dir} removed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Calling functions based on CLI arguments.
if sys.argv[1]=='install':
  install_redis()
elif sys.argv[1]=='start':
  start_redis()
elif sys.argv[1]=='check_status':
  check_redis_status()
elif sys.argv[1]=='restart':
   restart_redis()
elif sys.argv[1]=='stop':
   stop_redis()
elif sys.argv[1]=='backup':
   backup_redis()
elif sys.argv[1]=='uninstall':
   uninstall_redis()

#print('Help: ./system-metric.py {install|start|check_status|restart|stop|backup|uninstall}')