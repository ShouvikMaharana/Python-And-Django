class dsa_class:
    def iterate_dict_using_key(self,dict_sample):
        for i in dict_sample.keys():
            print(f"{i}:{dict_sample[i]}")

    def iterate_dict_using_item(self,dict_sample):
        for i,j in dict_sample.items():
            print(f"{i}:{j}")
        
    def iterate_list(self,list1):
        for i in range(len(list1)):
            print(f"{list1[i]}",end=" ")
    
    def append_at_begining_list(self,list1,targetv):
        list1.append(None)
        for i in range(len(list1)-1,0,-1):
            list1[i]=list1[i-1]
        list1[0]=targetv
        print(f"{list1[i]}",end=" ")
    
    def sum_of_items_in_2dlist(self,list2):
        sum=0
        for i in range(len(list2)):
            for j in range(len(list2[i])):
                sum+=list2[i][j]
        print(f"{list2}",end=" ")

    def sum_of_diagonals_in_2dlist(self,list2):
        sum=0
        for i in range(len(list2)):
            for j in range(len(list2[i])):
                if (i==j or i+j==len(list2)-1):
                    sum+=list2[i][j]
        print(f"{list2}",end=" ")
    
    def matrix_mul(self,list3,list4):
        list=[[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(list3)):
            for j in range(len(list3[i])):
                sum=0
                for k in range(len(list4[i])):
                    list[i][j]+=list3[i][k]*list4[k][j]
        print(f"{list}",end=" ")
    
    def matrix_sum(self,list3,list4):
        list=[]
        for i in range(len(list3)):
            for j in range(len(list3[i])):
                list.append(list3[i][j]+list4[i][j])
        print(f"{list}")

    def no_of_occurance_in_a_string(self,string1,targetv):
        c=0
        for i in range(len(string1)):
            if (targetv == string1[i]):
                c+=1
        print(c)

    def replace_dup(self,list5):
        b=[]
        for i in range(len(list5)):
            if(list5[i] not in b):
                b.append(list5[i])
        print(b)
    
dsa_obj=dsa_class()
dsa_obj.iterate_dict_using_key({1:"A",2:"B",3:"C"})
dsa_obj.iterate_dict_using_item({1:"A",2:"B",3:"C"})
dsa_obj.iterate_list([1,2,3,4,5,6,7,8,9])
dsa_obj.append_at_begining_list([1,2,3,4,5,6,7,8,9],10)
dsa_obj.sum_of_items_in_2dlist([[1,2,3],[4,5,6],[7,8,9]])
dsa_obj.sum_of_diagonals_in_2dlist([[1,2,3],[4,5,6],[7,8,9]])
dsa_obj.matrix_mul([[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]])
dsa_obj.matrix_sum([[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]])
dsa_obj.no_of_occurance_in_a_string("My name is Shouvik Maharana.","a")
dsa_obj.replace_dup([1,2,2,3,4,5,5,6,8,7,7,9,9,1,2,4,5,6,7,8,9])