from dataclasses import dataclass


@dataclass
class Product:
    name:str
    value_multiplier: float

@dataclass
class ProductStack:
    amount: float
    product: Product

class Market:
    def __init__(self, products: list[Product], stacks: list[ProductStack]) -> None:
        self.products = products
        self.stacks = stacks

    @property
    def product_names(self) -> list:
        """List of all unique names in products list."""
        return list(set([product.name for product in self.products]))

    @property
    def stacks_by_name(self) -> dict[str, list[ProductStack]]:
        """Sum all the same product stacks into a bigger one."""
        return {
            product_name: [
                stack for stack in self.stacks if product_name == stack.product.name
            ] for product_name in self.product_names
        }
    
    def get_total_amount_of_a_product(self, product_name:str) -> float:
        """Get total amount of a certain product in the marketing."""
        products = self.stacks_by_name[product_name]
        return sum([product.amount for product in products])

            
if __name__ == "__main__":
    rice_product = Product("rice", 1.5)
    rice_stack = ProductStack(500, rice_product)
    list_of_products = [rice_product]
    list_of_stacks = [
        rice_stack,
        rice_stack,
        rice_stack,
        rice_stack,
        rice_stack,
        rice_stack,
        rice_stack,
        rice_stack,
    ]
    market = Market(list_of_products, list_of_stacks)
    print(market.product_names)
    print(market.stacks_by_name)
    print(market.get_total_amount_of_a_product("rice"))