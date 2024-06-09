class Animal:
    def species_selection(self,number_of_legs,can_speak,is_a_baby):
        if number_of_legs==2 and can_speak==True:
            return 'Human'
        elif number_of_legs==4 and can_speak==False and is_a_baby==True:
            return 'Human Baby'
        else: 
            return 'Not Human'




object_1=Animal()
obj_1_output=object_1.species_selection(2,True,True)
print(obj_1_output)

object_2=Animal()
obj_2_output=object_2.species_selection(4,False,False)
print(obj_2_output)

object_3=Animal()
obj_3_output=object_3.species_selection(4,False,True)
print(obj_3_output)