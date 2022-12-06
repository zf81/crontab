Assignment # 6: crontab

Cron jobs:
Pull data down every day at 7:00 AM
0 7 * * * /user/bin/python3 /home/fizzahzaidi/crontab/healthAlz.py > log.txt 2<&1 &

Pull data every Sunday night at 10:00pm
0 22 * * SUN /user/bin/python3 /home/fizzahzaidi/crontab/healthAlz.py > log.txt 2<&1 &

Pull data at the end of every quarter
0 0 1 */3 * /user/bin/python3 /home/fizzahzaidi/crontab/healthAlz.py > log.txt 2<&1 &