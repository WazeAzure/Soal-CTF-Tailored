# Soal-CTF-Tailored

## Daftar Soal
No | Nama Soal | Platform | Attack | CVE? | Note
--- | --- | --- | --- | --- | ---
1 | [Zygot-PHP-1](#1-zygot-php-1) | Web | LFI | - | its baby
2 | [Web-File](#w2-eb-file) | Web | ??? | - | basic :V
3 | [Hide-Me-Part-1](#3-hide-me-part-1) | 4n6 | - | - | - | -
4 | [Infinite-Zip](#4-infinite-zip) | msc | - | - | - | -
5 | [Hello-Blockchain](#5-hello-blockchain) | blc | - | - | sepolia
6 | [Magic-Bytes-Blockchain](#6-magic-bytes-blockchain) | blc | - | - | sepolia
7 | [PhishHunt](#7-phishhunt) | 4n6 | - | - | adopted from hacktrace
----

# 1. Zygot-PHP-1
A simple Local File Inclusion :D. Probably too simple :v
```
Description:
Dr Can you find the flag?
```

# 2. Web-File
Simpel, cuman ngmabil flag yang scattered :v
```
Description:
Can you find the creds accross the web? then probably somehow, the flag is located in the default folder of web hosting :nerd:
```

# 3. Hide-Me-Part-1
tinggal strings :v
```
Description:
Find me. Im hidden in the file.
```

# 4. Infinite-Zip
tinggal unzip ampe mampus AOWKOAWK (scripting)
```
Description:
unzip sampe mampos awokawok.
```
# 5. Hello-Blockchain
Hello world tapi sepolia network :3
```
Description:
"Hello Blockchain" from the other side.
can you connect to the smartcontract?

contract address: 0xe1e604bf82D018D790AdEAB911E7445336aA6e73
network: sepolia
```
# 6. Magic-Bytes-Blockchain
hehehe 4 bytes signature hehehe.
```
Description:
can you find the flag function? from "bytecodes"?
Wrap it inside CTFITB{...} (e.g CTFITB{nama_fungsi_flag})

contract address: 0x62D4f0C9595f4439499F256AbE69974453898DB6
```
# 7. PhishHunt
email forensic
```
Description PART 1:
Pada hari Senin Ibu pergi ke kantor. Di kantor Ibu ketemu flash drive* tergeletak di meja kerjanya. Seingatnya flash drive tersebut merupakan milik temannya. Teman Ibu meminta bantuan untuk memeriksa apakah email yang ia dapatkan merupakan transaksi keuangan yang valid atau penipuan. Sayangnya, teman ibu lupa password dari file tersebut.

Cerita ini memang ga nyambung, jadi yasudahlah ya.
Bantulah Ibu mencapai tujuannya HORE :D

* namanya flashdrive, bukan flashdisk :(
* HATI-HATI ADA VIRUS BENERAN. JANGAN DIRUNNING SEMBARANGAN

nc x.x.x.x xx
============================================================================
Description PART 2:
Yey kamu berhasil membantu ibu untuk bagian pertama. SEKARANG BAGIAN KE 2.
Gutlak.

May the force be with you.

* HATI-HATI ADA VIRUS BENERAN. JANGAN DIRUNNING SEMBARANGAN

nc x.x.x.x xx
```
**PART 1**
1. Apa email pengirim?
alvawensz@hlsholding.com.cn
2. Apa email penerima?
admin@starlucktech.com
3. Alamat IP pengirim?
185.225.74.18
4. Berasal dari negara mana IP pengirim?
Netherlands / Belanda (translate ke indo)
5. Apa nama file lampiran pada email?
BANK DETAILS.pdf.zip

**PART 2**
1. Apa nilai md5 dari file lampiran?
f667f7c0f470a550b6cfbce4236b3be4
2. Apa nama file didalam file lampiran?
PO.pdf.exe
3. Apa nama asli file tersebut?
ZySG.exe
3. Malware jenis apa file tersebut?
Trojan
4. Apa nama domain yang berkomunikasi dengan malware?
api.ipify.org,api4.ipify.org