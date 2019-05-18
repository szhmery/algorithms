import os
import zipfile
import glob
import paramiko

if __name__ == "__main__":
    path = "/Users/zhaohsun/Downloads/sharefolder"
    filename = "test.txt"
    zipfilename= "/Users/zhaohsun/Downloads/destDir/test.zip"
    remoteFile = "/root/test.zip"

    # test login server successfully
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("10.124.100.195", 22, "root", "lab123")
    stdin, stdout, stderr = ssh.exec_command("ls")
    print(stdout.readlines())
    ssh.close()
    t = paramiko.Transport(("10.124.100.195", 22))
    t.connect(username="root", password="lab123")
    sftp = paramiko.SFTPClient.from_transport(t)

    for root, dirs, files in os.walk(path, topdown=False):
        if filename in files:
            file = os.path.join(root, filename)
            z = zipfile.ZipFile(zipfilename, 'w')
            print(file)
            z.write(file, filename)
            print(z.filelist)
            z.close()
            print(zipfilename)
            sftp.put(zipfilename, remoteFile)
    t.close()

    # os.system("cp " + os.path.join(root, filename) + " " + destDir)
    # pathList = glob.glob(os.path.join('/', path, "test.txt"))
    # print(pathList)
    # print(os.listdir(path))
    # for file in os.listdir(path):
    #     if file==filename:
    #         os.system("cp " + file + " " +destDir)
    #
