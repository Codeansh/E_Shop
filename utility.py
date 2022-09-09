
def find_product(id:int) -> int:
    for index,item in enumerate(products) :
        print(index)
        if item.get('id') == id :
            return index
    return None
