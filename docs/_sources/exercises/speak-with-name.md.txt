# Speak with Name

Take your code from the previous exercise and modify the speak method to include the animal's name in the output. The output should be in the format ``"The {name} speaks."``.

![Student UML](examples/uml-animal-speak.png)

## Starter code
```python
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    # place the instance method here (in the class)


dog = Animal("dog")
dog.speak()  # should output "The dog speaks"

cat = Animal("cat")
cat.speak()  # should output "The cat speaks"

```