import os
import zipfile
import glob
import paramiko

if __name__ == "__main__":
    path = "/Users/zhaohsun/Downloads/sharefolder"
    serachFileName = "test.txt"
    zipfilename= "/Users/zhaohsun/Downloads/destDir/test.zip"
    remoteFile = "/root/test.zip"
    server_ip = "192.168.1.1"

    # test login server successfully
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_ip, 22, "root", "***")
    stdin, stdout, stderr = ssh.exec_command("ls")
    print(stdout.readlines())
    ssh.close()

    #上传文件的方式和发送命令的方式不一样。
    t = paramiko.Transport((server_ip, 22))#记住是双括号
    t.connect(username="root", password="***")
    sftp = paramiko.SFTPClient.from_transport(t)

    for root, dirs, files in os.walk(path, topdown=False):
        if serachFileName in files:
            file = os.path.join(root, serachFileName)
            z = zipfile.ZipFile(zipfilename, 'w')
            print(file)
            z.write(file, serachFileName)
            print(z.filelist)
            z.close()
            print(zipfilename)
            sftp.put(zipfilename, remoteFile)
    t.close()

    #以上结束。下面是一些探索

    # 可以找到所有文件夹下符合该条件的文件
    pathList = glob.glob(os.path.join('/', path, "test*"))
    print(pathList)

    # 只能找当年目前下文件,不能文件夹内部文件夹遍历
    for file in os.listdir(path):
        if file == serachFileName:
            print(file)

