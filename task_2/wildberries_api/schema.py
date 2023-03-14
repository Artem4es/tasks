from pydantic import BaseModel, Field


class Product(BaseModel):
    """PyDantic object for product"""

    article: int = Field(alias='id')
    brand: str
    title: str = Field(alias='name')


class Data(BaseModel):
    products: list[Product]

    def __iter__(self):
        return iter(self.products)

    def __getitem__(self, item):
        return self.products[item]


class ModelItem(BaseModel):
    data: Data


class Model(BaseModel):
    __root__: list[ModelItem]

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, item):
        return self.__root__[item]


def create_pydantic(data):
    """Creates PyDantic object and returns list of objects"""
    products = []
    for i in range(len(data)):
        model = ModelItem.parse_raw(data[i])
        product = model.data.products
        products.append(product)

    return products
