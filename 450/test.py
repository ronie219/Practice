<<<<<<< HEAD
class Employee:

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self):
        return f'{self.name} having age of {self.age}'


if __name__ == '__main__':
    e1 = Employee("Rohit", 25)
    print(e1)
    setattr(e1, "name", "Satyam")
    print(e1)
    a = ["Abhishek",]
    print(isinstance(a, list))

    from itertools import islice

    print(islice("hello",2))
=======
import csv
person_id = {110051457:149764
,110046731:147584
,30022341:30022341
,120053873:385939
,30044175:30044175
,110012874:135069
,120085906:120085906
,120160262:1048635
,120106418:858542
,110061031:163963
,110059342:154984
,110059431:155063
,120020751:220796
,30018125:30018125
,120084585:798108
,110034024:143991
,30045734:30045734
,120123622:911747
,120097774:835231
,110061182:156581
,110051476:149776
,110047300:944652
,120111224:875841
,110047726:148082
,110034436:144260
,120035594:858399
,30004797:30004797
,120112432:20000805
,120105863:857271
,110046317:147376
,110050913:149429
,110048759:148571
,110006479:131919
,110046712:147570
,110058443:154343
,110041406:20000696
,120069514:431676
,120023274:227581
,110060990:156420
,120157531:1035757
,120053185:384304
,30015248:30015248
,120158166:1038894
,110055189:151943
,120061041:408517
,110060683:156150
,110047750:148101
,110061107:156521}
data = []
with open('doc.csv',mode='r') as file:
    reader = csv.DictReader(file)
    for ele in reader:
        data.append(ele)
# print(data)
for i in data:
    if int(i['ID #']) in person_id.keys() : i['PERSON_ID'] = str(person_id[int(i['ID #'])])

# for i in data:
#     print(i)


with open('update.csv',mode='w') as updated:

    fields = ['GONE','DEPT','ID #','PERSON_ID','NAME','O/P/N','COMMENTS','HRS','START_DATE','END_DATE']
    writer = csv.DictWriter(updated,fieldnames=fields)
    writer.writeheader()
    [writer.writerow(ele) for ele in data]
>>>>>>> 7f688d62f8ef42d5982882d6981075fb426ea81a
