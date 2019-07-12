class Codemeli:
    def __init__(self,num):
        self.num=num

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self,value):

        if len(value)==10 :
            
            if isinstance(value,str):
                if value.isdigit():
                    self.__num=value
                else:
                    raise ValueError('Your codemeli should be integer!')
            else:
                raise TypeError('Your codemeli should be integer!')
        else:
            print('Codemeli should be 10 number!')

    def check_codemeli(self):
        
        counter = 2
        sp=0

        x=self.num[::-1]
        for i in range(1,len(x)):
            sp+=int(x[i])*counter
        
            counter+=1
        if sp%11<2 and sp%11 == int(self.num[-1]):
            print('Codemeli is true')
        elif 11-(sp%11) == int(self.num[-1]):
            print('Codemeli is true!')
        else:
            print('Codemeli is wrong!')
        
code=Codemeli(input('>>'))
code.check_codemeli()