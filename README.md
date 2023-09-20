# odoo16_nimdasx

## shell

```shell
#masuk ke virtualenv
source mayat/bin/activate

#run tanpa masuk ke virtualenv
./mayat/bin/python blablablbal

#run community
odoo/odoo-bin -c konfig_community.conf 

#run enterprise
odoo/odoo-bin -c konfig_enterprise.conf

#update all module
odoo/odoo-bin -c konfig_community.conf -u all -d odoo16_community_01

#update single module
odoo/odoo-bin -c konfig_community.conf -u nimdasx_health -d odoo16_community_01

#biar gak perlu reload -u kalau ngedit view
 ./odoo-bin -d rd-demo -u estate --dev xml

```

## bug

*bug 01 : 15 sept 2023*
1. upgrade/install pertama semua record child (sfx_bug) berhasil diimport (ok)
2. upgrade/install kedua, smua record child (sfx_bud) kok malah ilang (fail)
3. upgrade/install ketiga, semua record child (sfx_bug) berhasil terimport lagi (ok)
4. begitu seterusnya

sudah ada solusi, pisahkan childnya (sfx_bug) di file sendiri  
sfx_obat.00.csv tidak dipakai, ganti dengan 2 filx sfx_obat.csv dan sfx_bud.csv  

## catatan

### buat translation
1. settings -> translations -> export translation :  
   - language : new language (empty translation template)
   - file format : PO File
   - Apps to Export : sfx_health
2. taruh di sfx_health/i18n
3. buka sfx_health/i18n/sfx_health.pot menggunakan POEDIT
4. create new translation, pilih Indonesia, save di i18n, lakukan edit2
5. tambahkan parameter --i18n-overwrite di odoo run
6. pakai _("adsadbl") jika tidak terdeteksi di POT file