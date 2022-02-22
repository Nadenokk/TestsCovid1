#!/usr/bin/env python
#coding:utf-8
 # Добро пожаловать в публичный аккаунт WeChat: технология Bit by Bit
 # Вот надежные, ценные и растущие вместе, эксклюзив для сетевой осады льва

import paramiko, time
from paramiko.ssh_exception import NoValidConnectionsError,AuthenticationException

def ssh_client(host, user, cmds, verbose=True):
         # Путь для хранения файла закрытого ключа
    private = paramiko.RSAKey.from_private_key_file(r'C:\Users\wd10\PycharmProjects\TestsCov\med\id_rsa')
         # Создаем экземпляр
    ssh = paramiko.SSHClient()
         # Загрузить системный SSH-ключ
    ssh.load_system_host_keys()
         # Автоматически добавлять стратегию, сохранять имя хоста сервера и ключевую информацию, если вы не добавите, то хост, который не записан в локальном файле know_hosts, не сможет подключиться, и значение по умолчанию будет отклонено
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
         # Подключить устройство
    try:
        ssh.connect(hostname=host,
                    port=443,
                    username=user,
                    timeout=5,
                    compress=True,
                    pkey = private, # можно использовать подключение по ключу
                    )

        print ("Подключение к хосту {} .....")
        ssh.open_sftp()

    except NoValidConnectionsError:
                     print ('Проблема с подключением')
    except AuthenticationException:
                     print ('Неверное имя пользователя или пароль')
    except Exception as e:
                     print ('Другие проблемы с ошибками {)')
    finally:
                     # Активировать интерактивную оболочку
        chan = ssh.invoke_shell()
        time.sleep(1)

        for cmd in cmds:
            chan.send(cmd.encode())
                         # Должен быть возврат каретки 'Enter' это действие
            chan.send(b'\n')
            time.sleep(2)
            r = chan.recv(40960).decode()
            if verbose:
                print(r)
        chan.close()
        ssh.close()

def sftp_get(ip, user, pwd, local_file,remote_file, port=22):
    try:
        t = paramiko.Transport(ip, port)
        t.connect(username=user, password=pwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(remote_file, local_file)
        t.close()

    except Exception as e:
        print(e)


def sftp_put(ip, user, pwd, local_file, remote_file, port=22):
    try:
        t = paramiko.Transport(ip, port)
        t.connect(username=user, password=pwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(local_file, remote_file)
        t.close()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    '''
         Не запускайте, закомментируйте и добавьте символ «#» впереди
    '''
    ip = '195.19.96.255'
    user= 'nadya'
    #pwd= 'Admin@123'
    # local_file = r'D:\test\123.txt'
    # remote_file = 'flash:/vrpcfg.zip'
    # sftp_get(ip='192.168.0.200', user=user, pwd=pwd, remote_file=remote_file, local_file=r'D:\test\vrpcfg.zip')
    # sftp_put(ip='192.168.0.200', user=user, pwd=pwd, local_file=local_file, remote_file='flash:/123.txt')

    cmds = [ 'cd /opt/wildfly/standalone/tmp/report/aids/022022', 'ls -la']
    # cmds = ['disp ip int br','disp device','disp clock']
    ssh_client(ip, user, cmds)