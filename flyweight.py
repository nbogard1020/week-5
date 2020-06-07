Class Pizza(object):
    
    def __init__(self):
  
        pass
  
    defpizza(self, pizza_type):
  
        return "ComplexPattern[% s]" % (pizza_type)
  
  
Class PizzaSizes(object):
    
    Pizza_sizes = {}
  
    def __new__(piz, name, pizza_size_id):
        try:
            id = piz.pizza_size[pizza_size_id]
        except KeyError:
            id = object.__new__(piz)
            piz.pizza_size[pizza_size_id] = id
        return id
  
    def set_pizza_info(self, pizza_info):
  
  
        pi =PizzaInformation()
        self.piz_info = piz.pizza(pizza_info)
  
    def get_pizza_info(self):
    
        return (self.pizza_info)
    
  
if __name__ == '__main__':
    pizza_data = (('P', 1, 'Large'), ('P', 2, 'Medium'), ('P', 1, 'Small'))
    pizza_size_objects = []
    for i in pizza_data:
        obj =PizaSizes(i[0], i[1])
        obj.set_pizza_info(i[2])
        pizza_size_objects.append(obj)
    
    for i in pizza_size_objects:
        print("id = " + str(id(i)))
        print(i.get_pizza_info())

