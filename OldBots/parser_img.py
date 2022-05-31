import os  # importing all we need, it's not much
import wget

urls_to_load = list()  # a list to store the urls
path = 'download_folder'  # the path where we will download those files
a = "https://member.etn-net.org/magazines/en/2001/ETN-TF_4-2001_EN/ETN-TF_4-2001_EN_01.jpg"  # the first two images are separate as the source has them named differently
b = "https://member.etn-net.org/magazines/en/2001/ETN-TF_4-2001_EN/ETN-TF_4-2001_EN_31.jpg"
urls_to_load.extend([a, b])  # add them to the url list
# add all other images, generating their names as we need
for i in range(2,
               31):  # it is important to make this second number +1, so PY makes the list correctly (as far as we start with 2)
    a = "https://member.etn-net.org/magazines/en/2001/ETN-TF_4-2001_EN/ETN-TF_4-2001_EN_" + str(i).zfill(2) + "a.jpg"
    b = "https://member.etn-net.org/magazines/en/2001/ETN-TF_4-2001_EN/ETN-TF_4-2001_EN_" + str(i).zfill(2) + "b.jpg"
    urls_to_load.extend([a, b])
# preparing to download
if not os.path.exists(path):
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)
# starting to download
print("Starting downloading")
for url in urls_to_load:
    file_name = path + '/' + os.path.basename(url)  # get the full path to the file
    if os.path.exists(file_name):
        os.remove(file_name)  # if exists, remove it directly
    file_name = wget.download(url, out=path)
    print(file_name)
print("ok")
