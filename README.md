# odoo16_nimdasx

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

```