class CutestCats:
    def __init__(self,name,description,averageweight,averagelength,averagelifeexpectancy,imageurl):
        self.__name = name
        self.__description = description
        self.__averageweight = averageweight
        self.__averagelength = averagelength
        self.__averagelifeexpectancy = averagelifeexpectancy
        self.__imageurl = imageurl    
    
    def GetCatDetails(self):
        return (self.__name, self.__description, self.__averageweight,self.__averagelength,self.__averagelifeexpectancy,self.__imageurl)
    
    def GetCatLife(self):
        return 'Name: ' + str(self.__name) + '\nLife expectancy: ' + str(self.__averagelifeexpectancy)
    
cat_database = []
with open('CutestCatsSimple.txt','r') as f:
    num_lines = len(f.readlines())
    f.seek(0)
    for i in range(num_lines//6):
        cat_name = f.readline().strip()
        cat_desc = f.readline().strip()
        cat_weight = f.readline().strip()
        cat_weight_list = cat_weight.split(' ')
        total=0
        count = 0
        for i in cat_weight_list:
            if i.isdigit():
                total += int(i)
                count += 1
        cat_averageweight = total/count
        total=0
        count = 0
        cat_length = f.readline().strip()
        cat_length_list = cat_length.split()
        for i in cat_length_list:
            if i.isdigit():
                total += int(i)
                count += 1
        cat_averagelength = total/count
        total=0
        count = 0
        cat_lifeexp = f.readline().strip()
        cat_lifeexp_list = cat_lifeexp.split()
        for i in cat_lifeexp_list:
            if i.isdigit():
                total += int(i)
                count += 1
        cat_averagelifeexp = total/count
        cat_image = f.readline().strip()
        cat_database.append(CutestCats(cat_name,cat_desc,cat_averageweight,cat_averagelength,cat_averagelifeexp,cat_image))

def sort_life_exp(table):
    life_exp = []
    for i in table:
        life_exp.append(i.GetCatDetails()[4])
        
    line = ''
    x = sorted(life_exp)
    for i in x:
        for j in table:
            if i == j.GetCatDetails()[4]:
                line += j.GetCatLife() +'\n'
    return line

print("Cats sorted based in life expectancy (ascending):")
print(sort_life_exp(cat_database))
