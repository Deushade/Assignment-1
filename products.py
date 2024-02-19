# Program Name: Product Data Manipulation & Analysis
# Program Date: February 18th, 2024
# Program Author: Leigh McElmon

# Program Description: The purpose of this program, is to read products from a text file, where we can store it in a dynamic array. To explore data manipulation and sorting techniques, many functions are made to accomodate like insert, delete, update,
# search, and quicksort. Once these techniques are shown, the execution time is recorded for a list that is ordered, and when the list is reverse ordered.


import time

# Creating a main class for the data where we will initialize the array for the products
class ProductManager:
    def __init__(self):
        # Array is initialized as empty
        self.products = []

    # Creating a function that will load the products from the product_data.txt file
    def load_products(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                # The lines in the file are loaded and split up by commas with the appropriate attributes for the data
                id, name, price, category = line.strip().split(', ')
                # The data is appended to the products array
                self.products.append({
                    'ID': id,
                    'Name': name,
                    'Price': float(price),
                    'Category': category
                })

    # Creating a function so the productsa in the product array can print
    def display_products(self):
        for product in self.products:
            print(product)

    # Creating a function that will insert a new product, with the same parameters as the other products
    def insert_product(self, id, name, price, category):
        # The new product or products is appended into the array
        self.products.append({'ID': id, 'Name': name, 'Price': price, 'Category': category})

    # Creating a function to update a product based on the the id of the strings
    def update_product(self, id, **kwargs):
        for product in self.products:
            if product['ID'] == id:
                product.update(kwargs)
                return True
        return False

    # Creating a function that will delete the product based on the ID
    def delete_product(self, id):
        self.products = [product for product in self.products if product['ID'] != id]

    # Creating a function that will search the array for a product based on the name or id
    def search_product(self, **criteria):
        results = []
        for product in self.products:
            if all(product.get(k) == v for k, v in criteria.items()):
                results.append(product)
        return results

    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)

    def partition(self, low, high):
        pivot = self.products[high]['Price']
        i = low - 1
        for j in range(low, high):
            if self.products[j]['Price'] <= pivot:
                i += 1
                self.products[i], self.products[j] = self.products[j], self.products[i]
        self.products[i + 1], self.products[high] = self.products[high], self.products[i + 1]
        return i + 1

    # Creates a function where an array can be reverse in its order
    def reverse_products(self):
        self.products.reverse()

    # Creating a function to measure the operations for sorted and reverse sorted time complexity
    def measure_sort_times(self):
        # Number so repitions so it can display a somewhat accurate execution time
        repetitions = 100 

        # Starts the performance counter for the array in a range of repetitions (100)
        start_time = time.perf_counter()
        for _ in range(repetitions):
            # Quicksort is applied to all of the repetitons
            self.quick_sort(0, len(self.products) - 1)
        # The timer is ended for quick sort
        end_time = time.perf_counter()
        # variable is made to store the average time of one operation, by dividing the total time by the repetitions (100)
        sorted_time = (end_time - start_time) / repetitions
        # Prints a string of text with some variables that display the average time complexity from 100 executions
        print(f"The time to sort already sorted data averaged over {repetitions} executions is: {sorted_time:.10f} seconds.")
        
        # Reversing the sorted array with the reverse_products function made earlier
        self.reverse_products()
        
        # Starts the performance counter for the reverse array in a range of repetitions (100)
        start_time = time.perf_counter()
        for _ in range(repetitions):
            # Quick sort is applied to all of the repititions of the reversed array
            self.quick_sort(0, len(self.products) - 1)
        # End timer is added
        end_time = time.perf_counter()
        # Average is made by divide the time by the total repetitions (100)
        reverse_sorted_time = (end_time - start_time) / repetitions
        print(f"The time to sort reverse ordered data averaged over {repetitions} exectutions is: {reverse_sorted_time:.10f} seconds.")


# Calling the main class that acts as a manager
manager = ProductManager()
# Load function that open the text file product_data.txt with the appropriate attributes
manager.load_products('product_data.txt')


# Calling the insert function where a new product can be added to the array  
# manager.insert_product('12345', 'Computer', 899.99, 'Electronics')
# Calling the update function to change the price of the computer product id that was previously added
# manager.update_product('12345', Price=799.99)
# Calling the delete function to delete a product from the array (Camera VFQWS)
# manager.delete_product('62422')
# Calling the search function to find a product from the array
# search_results = manager.search_product(Name='Mystery BOPTP')
# Prints the results from the search_products function
# print("Search Results:", search_results)

# Calling the quick sort function that will sort of the products by price
manager.quick_sort(0, len(manager.products) - 1)
# Prints all of the products from the file plus the operations
manager.display_products()

# Prints a string of text for the Complexity Analysis
print("\nComplexity Analysis:")
# Calls the measure sort times function to display the average execution times for a sorted and reverse sorted list
manager.measure_sort_times()
