#! /usr/bin/env python3

f = open("output.txt", 'r')

inp = f.read()
arr = inp.split("\n")
num = 0

for e in arr:
    d = dict()
    el = e.split(" ")
    for ee in el:
        if ee == "":
            continue
        kk = ee.split(":")
        d[kk[0]] = kk[1]


    try:    
        # task1
        leng = len(d.keys()) 
        if leng < 7 or leng > 8:
            continue
        if len == 7:
            if "cid" in d.keys():
                continue

        # task2 
        byr = int(d['byr'])
        if byr < 1920 or byr > 2002:
            continue

        iyr = int(d['iyr'])
        if iyr < 2010 or iyr > 2020:
            continue

        eyr = int(d['eyr'])
        if eyr < 2020 or eyr > 2030:
            continue

        hgt = d['hgt']
        if hgt.endswith("cm"):
            hgt = int(hgt[0:-2])
            if hgt < 150 or hgt > 193:
                continue
        elif hgt.endswith("in"):
            hgt = int(hgt[0:-2])
            if hgt < 59 or hgt > 76:
                continue
        else:
            continue

        hcl = d['hcl']
        if not hcl.startswith("#"):
            continue
        try:
            x = int(hcl[1:], 16)
        except ValueError:
            continue

        pid = d['pid']
        if not len(pid) == 9 or not pid.isdigit():
            continue
           
        eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if d['ecl'] not in eyecolors:
            continue

        num = num + 1  

    except KeyError:

        continue

print(num)
