# odoo16_nimdasx

```shell
#masuk ke virtualenv
source mayat/bin/activate

#run community
./mayat/bin/python odoo/odoo-bin -c konfig_community.conf
odoo/odoo-bin -c konfig_community.conf 

#run enterprise
./mayat/bin/python odoo/odoo-bin -c konfig_enterprise.conf
odoo/odoo-bin -c konfig_enterprise.conf

#update all module
./mayat/bin/python odoo/odoo-bin -c konfig_community.conf -u all -d odoo16_community_01

#update single module
odoo/odoo-bin -c konfig_community.conf -u nimdasx_health -d odoo16_community_01

```