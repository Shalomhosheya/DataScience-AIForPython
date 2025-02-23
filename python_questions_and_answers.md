
# Python Questions and Answers

1. **How can you generate a random integer between 1 and 100 in Python?**
   - `import random; random.randint(1, 100)`

2. **What is the purpose of the pandas DataFrame in data analysis?**
   - It is used for storing and manipulating structured data in tabular form (rows and columns).

3. **Explain the role of the Python interpreter.**
   - The Python interpreter executes Python code line by line, translating it into machine code.

4. **What are Python's built-in file handling methods for reading and writing files?**
   - `open()`, `read()`, `write()`, `close()`

5. **What is polymorphism in Python? Give an example.**
   - Polymorphism allows methods to have different behaviors based on the object type. Example: 
     ```python
     class Animal:
         def speak(self):
             print("Animal speaks")
     class Dog(Animal):
         def speak(self):
             print("Dog barks")
     ```

6. **What is the purpose of the super() function in Python OOP?**
   - It is used to call a method from the parent class.

7. **What is the purpose of the shape attribute in a NumPy array?**
   - It returns a tuple representing the dimensions of the array.

8. **What is the purpose of the head() and tail() methods in pandas?**
   - `head()` returns the first 5 rows, and `tail()` returns the last 5 rows of a DataFrame.

9. **How do you filter rows in a pandas DataFrame based on a condition?**
   - Use boolean indexing, e.g., `df[df['column'] > value]`.
