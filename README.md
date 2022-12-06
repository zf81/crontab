Assignment # 6: crontab

Cron jobs:
Pull data down every day at 7:00 AM
0 7 * * * /user/bin/python3 /home/fizzahzaidi/crontab/healthAlz.py > log.txt 2<&1 &

Pull data every Sunday night at 10:00pm
0 22 * * SUN /user/bin/python3 /home/fizzahzaidi/crontab/healthAlz.py > log.txt 2<&1 &

Pull data at the end of every quarter
0 0 1 */3 * /user/bin/python3 /home/fizzahzaidi/crontab/healthAlz.py > log.txt 2<&1 &


Created a VM through Azure (CRON_scratchmachine_group)
Used VM IP, username, and password to connect to VM through own terminal
sudo apt-get update
git clone (inserted URL of repository)
$ crontab -h
$ ls -l
$ cd crontab
$ pwd
$ nano healthAlz.py
$ crontab -e
Picked [1] from 1-4
Inserted cron job parameters from above 
Saved (^O) and exited (^X)
$ systemctl status cron
