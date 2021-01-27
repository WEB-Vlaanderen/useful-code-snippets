# Useful debugging tips

You've probably used console.log plenty of times. It’s the way to go when it comes to debugging for many web developers. But did you know that there are a lot more helpful functions available?

```javascript
console.count(); // prints the number of times this function is called
console.count();
console.count();
```

Output
```
default: 1
default: 2
default: 3
```

Even more useful is to pass a label to the function

```javascript
console.count("Name"); // prints the number of times the count function is called with label "Name"
console.count("Hello");
console.count("Name");
```

Output
```
Name: 1
Hello: 1
Name: 2
```

Credit: https://levelup.gitconnected.com/8-tricks-for-web-developers-you-can-put-into-practice-immediately-98079e65fd7d
