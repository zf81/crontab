Assignment # 6: crontab <br>

Cron jobs: <br>
Pull data down every day at 7:00 AM <br>
0 7 * * * /user/bin/python3 /home/fizzahzaidi/crontab/healthAlz.py > log.txt 2<&1 &   <br>

Pull data every Sunday night at 10:00pm <br>
0 22 * * SUN /user/bin/python3 /home/fizzahzaidi/crontab/healthAlz.py > log.txt 2<&1 &   <br>

Pull data at the end of every quarter <br>  
0 0 1 */3 * /user/bin/python3 /home/fizzahzaidi/crontab/healthAlz.py > log.txt 2<&1 &   <br>


Created a VM through Azure (CRON_scratchmachine_group) <br>
Used IP address of VM, username, and password to connect to VM on local terminal <br>
$ sudo apt-get update <br>
git clone (inserted URL of repository) <br>
$ crontab -h <br>
$ ls -l <br>
$ cd crontab <br> 
$ pwd <br>
$ nano healthAlz.py <br>
$ crontab -e <br>
Picked [1] from 1-4 <br>
Inserted cron job parameters from above <br>
Saved (^O) and exited (^X) <br>
$ systemctl status cron <br>
