import zipfile
import os

# zf = zipfile.ZipFile('2000.zip', "w")
# zf.write('flag.txt', compress_type=zipfile.ZIP_DEFLATED)
# zf.close()

for i in range(1999, -1, -1):
    zip_file = zipfile.ZipFile(f'{i}.zip', 'w')
    zip_file.write(f'{i+1}.zip', compress_type=zipfile.ZIP_DEFLATED)
    zip_file.close()