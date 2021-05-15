import csv

fm = ['ID:', 'Name:', 'Roll:', 'Marks:', 'Percent:', 'Remark:']
def copyfile(source_file,dest_file):
    with open(source_file,"r",newline="") as sf:
        with open(dest_file,"w",newline="") as df:
            cr=csv.DictReader(sf,fieldnames=fm)
            cw=csv.DictWriter(df,fieldnames=fm)
            cw.writeheader()
            for data in cr:
                cw.writerow(data)
def copydic(dest_file,dic):
    with open(dest_file,"a",newline="") as df:
        cw=csv.DictWriter(df,fieldnames=fm)
        cw.writerow(dic)
# s="student.csv"
# c="copy.csv"
# copy(s,c)