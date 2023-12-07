#1
class Palindrome:
    def __init__(self):
        self.stack = []

    def is_palindrome(self, text):
        text = ''.join(text.split()).lower()
        
        for char in text:
            self.stack.append(char)

        reversed_text = ''
        while self.stack:
            reversed_text += self.stack.pop()

        return text == reversed_text

input_text = input("Enter a string to check if it's a palindrome: ")
palindrome_checker = Palindrome()

if palindrome_checker.is_palindrome(input_text):
    print(input_text,"is a palindrome!")
else:
    print(input_text,"is not a palindrome.")


#2
from collections import deque

def is_balanced(expression):
    stack = deque()

    parentheses_mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in parentheses_mapping.values():
            stack.append(char)
        elif char in parentheses_mapping.keys():
            if not stack or stack.pop() != parentheses_mapping[char]:
                return False
        else:
            continue

    # The expression is balanced if the stack is empty at the end
    return not stack

input_expression = input("Enter an expression with parentheses to check if it's balanced: ")

if is_balanced(input_expression):
    print(f"The expression '{input_expression}' is balanced!")
else:
    print(f"The expression '{input_expression}' is not balanced.")


#3

def decode_message(encoded_message):
    stack = []

    for char in encoded_message:
        if char == '*':
            while stack:
                stack.pop()
        elif char.isalpha() or char.isspace():
            # Push alphabetical characters and white spaces onto the stack
            stack.append(char)

    decoded_message = ''.join(stack)
    return decoded_message

# Example usage
encoded_message = "SILVE***DAED TNSI **"
decoded_message = decode_message(encoded_message)

print(f"Encoded Message: {encoded_message}")
print(f"Decoded Message: {decoded_message}")


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, city1, city2):
        if city1 not in self.graph:
            self.graph[city1] = []
        self.graph[city1].append(city2)

        if city2 not in self.graph:
            self.graph[city2] = []
        self.graph[city2].append(city1)

    def has_route(self, start, end):
        visited = set()
        return self._has_route(start, end, visited)

    def _has_route(self, current, end, visited):
        visited.add(current)

        if current == end:
            return True

        for neighbor in self.graph.get(current, []):
            if neighbor not in visited:
                if self._has_route(neighbor, end, visited):
                    return True

        return False

    def print_directly_reachable(self, city):
        neighbors = self.graph.get(city, [])
        if neighbors:
            print(f"Directly reachable cities from {city}: {', '.join(neighbors)}")
        else:
            print(f"{city} has no directly reachable cities.")

# Function to check if parentheses are balanced
def are_parentheses_balanced(expression):
    stack = []

    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False  
            stack.pop()

    return not stack  

# Example usage of the Graph class and parentheses balancing function
my_graph = Graph()
my_graph.add_edge("CityA", "CityB")
my_graph.add_edge("CityB", "CityC")
my_graph.add_edge("CityC", "CityD")
my_graph.add_edge("CityD", "CityE")

print(my_graph.has_route("CityA", "CityD")) 
print(my_graph.has_route("CityA", "CityF"))  

my_graph.print_directly_reachable("CityB")  
my_graph.print_directly_reachable("CityE")  
my_graph.print_directly_reachable("CityF") 

expression = input("Enter an expression with parentheses to check if they are balanced: ")
result = are_parentheses_balanced(expression)

if result:
    print(f"The parentheses in '{expression}' are balanced.")
else:
    print(f"The parentheses in '{expression}' are not balanced.")



class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append(node2)

        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node2].append(node1)

    def has_cycle(self):
        visited = set()

        for node in self.graph:
            if node not in visited:
                if self._has_cycle(node, visited, parent=None):
                    return True

        return False

    def _has_cycle(self, node, visited, parent):
        visited.add(node)

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self._has_cycle(neighbor, visited, node):
                    return True
            elif parent != neighbor:
                return True

        return False

my_graph = Graph()
my_graph.add_edge(1, 2)
my_graph.add_edge(2, 3)
my_graph.add_edge(3, 4)
my_graph.add_edge(4, 1)

if my_graph.has_cycle():
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")
