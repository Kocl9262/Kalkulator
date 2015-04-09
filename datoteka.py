#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = float(raw_input("Vstavi prvo številko"))
y = float(raw_input("Vstavi drugo številko"))
znak = float(raw_input("Za seštevanje vpiši 1, za odštevanje vpiši 2, za množenje vpiši 3, za deljenje vpiši 4"))


if znak == 1:
    print(x + y)
elif znak == 2:
    print(x - y)
elif znak == 3:
    print(x * y)
elif znak == 4:
    print(x / y)
else:
    print("Error")
