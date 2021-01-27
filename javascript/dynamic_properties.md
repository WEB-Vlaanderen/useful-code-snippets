# Dynamic properties

There are times where you find yourself in a situation where you need to add dynamic properties to an object (a dynamic property is a property of which the key comes form a variable and may therefore be different for objects of the same type). Luckily, this is possible in JavaScript. In fact, there are several ways to do this.
This is what the first way looks like:

```javascript
const dynamic = 'name'
const person = {
    age: 33,
    [dynamic]: 'John'
}
```

It’s good to know that you can also combine dynamic properties with interpolation if you’re using ES6.
Let’s take a look at the following example where we’ve added an extra property to the person object using interpolation.

```javascript
const dynamic = 'name'
const person = {
    age: 33,
    [dynamic]: 'John',
    [`interpolated-${dynamic}`]: true
}
```

The last way to add a dynamic property to an object is by setting it in the same way as you would add a key-value pair to an array.

```javascript
const dynamic = 'name'
let person = {
    age: 33,
}
person[dynamic] = 'John'
```

The big advantage that this method has is that it allows you to not only add dynamic properties when declaring an object. This way of adding dynamic properties often gets used in combination with if-statements.

```javascript
let person = {
    age: 33,
}
if (someCondition) {
  person[someProperty] = someValue
}
```

Credit: https://levelup.gitconnected.com/8-tricks-for-web-developers-you-can-put-into-practice-immediately-98079e65fd7d
