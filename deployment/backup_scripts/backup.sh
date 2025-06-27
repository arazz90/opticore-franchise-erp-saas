#!/bin/bash
DATE=$(date +%F)
mysqldump -u root -proot --all-databases > /backup/all_db_backup_$DATE.sql
tar -czvf /backup/sites_backup_$DATE.tar.gz /home/frappe/frappe-bench/sites
