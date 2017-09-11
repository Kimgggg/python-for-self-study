#!/usr/bin/env python
# encoding: utf-8

debug_server = ["http://192.168.5.207:8001/demo/ctrl.php","http://192.168.5.206:8001/demo/ctrl.php","http://192.168.5.208:8001/demo/ctrl.php","http://123.207.86.208:8001/demo/ctrl.php","http://118.89.35.160:8001/demo/ctrl.php"]
dev_server = raw_input("please input debug server:\n")
dev_server = debug_server[int(dev_server)-1]
print dev_server