class supermercado():
    def __init__(self):
        self.productos_lacteos = []
        self.productos_aseo = []
        self.productos_granos = []
        
        self.productos_aseo_existencia =[]
        self.produtos_lacteos_existencia = []
        self.productos_granos_existencia = []
        
        
    def ingresar_productos(self):
        while True:
            tipo = str(input('Ingresa la categorìa del producto (lacteo, aseo, grano), ingrese "alto" si quiere parar: '))
            if(tipo=="lacteo"):
                self.ingresar_producto_lacteo()     
            if(tipo=="aseo"):
                self.ingresar_producto_aseo()
            if(tipo=="grano"):
                self.ingresar_producto_grano()
            if(tipo=="alto"):
                break
            
            
    
    
    def ingresar_producto_lacteo(self):      
        try:
            cantidad = int(input(' cuantos productos quiere ingresar: '))
            contador = 0
            while contador < cantidad:
                producto = input('ingrese el nombre del producto: ')
                posicion = self.buscar_producto_lacteo(producto)
                if(posicion == -1):
                    try:    
                        cantidad_existencia = int(input('ingrese la cantidad existente de estos productos'))
                        self.productos_lacteos.append(producto)
                        self.produtos_lacteos_existencia.append(cantidad_existencia)
                    except:
                        print('ingrese un numero por favor3')
                else:
                    try:
                        print('el producto ya existe \n agregando cantidad de productos')
                        cantidad_existencia = int(input('ingrese la cantidad existente de estos productos'))
                        self.produtos_lacteos_existencia[posicion] += cantidad_existencia
                    except:
                        print('por favor ingrese un numero2')
                contador += 1
        except:
            print('porfavor ingrese un numero1')
    
    
    def ingresar_producto_grano(self):
        try:
            cantidad = int(input(' cuantos productos quiere ingresar: '))
            contador = 0
            while contador < cantidad:
                producto = input('ingrese el nombre del producto: ')
                posicion = self.buscar_producto_grano(producto)
                if(posicion == -1):
                    try:
                        cantidad_existencia = int(input('ingrese la cantidad existente de estos productos'))
                        self.productos_granos.append(producto)
                        self.productos_granos_existencia.append(cantidad_existencia)
                    except:
                        print('por favor ingrese un numero')
                else:
                    try:
                        print('el producto ya existe \n agregando cantidad de productos')
                        cantidad_existencia = int(input('ingrese la cantidad existente de estos productos'))
                        self.productos_granos_existencia[posicion] += cantidad_existencia
                    except:
                        print('por favor ingrese un numero')
                contador += 1
        except:
            print('por favor ingrese un numero')
    
    
    def ingresar_producto_aseo(self):
        try:
            cantidad = int(input(' cuantos productos quiere ingresar: '))
            contador = 0
            while contador < cantidad:
                producto = input('ingrese el nombre del producto: ')
                posicion = self.buscar_producto_aseo(producto)
                if(posicion == -1):
                    try:
                        cantidad_existencia = int(input('ingrese la cantidad existente de estos productos'))
                        self.productos_aseo.append(producto)
                        self.productos_aseo_existencia.append(cantidad_existencia)
                    except:
                        print('por favor ingreseun numero')
                else:
                    try:
                        print('el producto ya existe \n agregando cantidad de productos')
                        cantidad_existencia = int(input('ingrese la cantidad existente de estos productos'))
                        self.productos_aseo_existencia[posicion] += cantidad_existencia
                    except:
                        print('por favor ingrese un numero')    
                contador += 1
        except:
            print('por favor ingrese un numero')
          
    
    def buscar_producto_lacteo(self, nombre_producto):
        contador = 0
        posicion = -1
        while posicion == -1 and contador < len(self.productos_lacteos):
            if(nombre_producto == self.productos_lacteos[contador]):
                posicion = contador
            contador += 1
        return posicion
    
    
    def buscar_producto_aseo(self, nombre_producto):
        contador = 0
        posicion = -1
        while posicion == -1 and contador < len(self.productos_aseo):
            if(nombre_producto == self.productos_aseo[contador]):
                posicion = contador
            contador += 1
        return posicion
        
    
    def buscar_producto_granos(self, nombre_producto):
        contador = 0
        posicion = -1
        while posicion == -1 and contador < len(self.productos_granos):
            if(nombre_producto == self.productos_granos[contador]):
                posicion = contador
            contador += 1
        return posicion
    
    
    def mostrar_info_productos(self):
        print('productos lacteos: \n')
        print(self.productos_lacteos)
        print(self.produtos_lacteos_existencia)
        print('productos de aseo: \n')
        print(self.productos_aseo)
        print(self.productos_aseo_existencia)
        print('productos granos: \n')
        print(self.productos_granos)
        print(self.productos_granos_existencia)
