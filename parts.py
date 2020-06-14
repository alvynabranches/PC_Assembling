class Product:
    def __init__(self, product_id, product_name, product_company):
        self.product_id = product_id
        self.product_name = product_name

    def __str__(self):
        return f"{self.product_name}"

class Motherboard(Product):
    def __init__(self, product_id, product_name, product_company):
        super().__init__(product_id, product_name, product_company)

    def __str__(self):
        return super().__str__()

class Processor(Product):
    def __init__(self, product_id, product_name, product_company):
        super().__init__(product_id, product_name, product_company)
    
    def __str__(self):
        return super().__str__()

class GPU(Product):
    def __init__(self, product_id, product_name, product_company):
        super().__init__(product_id, product_name, product_company)

    def __str__(self):
        return super().__str__()

class TPU(Product):
    def __init__(self, product_id, product_name, product_company):
        super().__init__(product_id, product_name, product_company)

    def __str__(self):
        return super().__str__()

class PowerSupply(Product):
    def __init__(self, product_id, product_name, product_company):
        super().__init__(product_id, product_name, product_company)

    def __str__(self):
        return super().__str__()

class RAM(Product):
    def __init__(self, product_id, product_name, product_company):
        super().__init__(product_id, product_name, product_company)

    def __str__(self):
        return super().__str__()