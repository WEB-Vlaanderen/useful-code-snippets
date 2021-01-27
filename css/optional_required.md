# Opional/required styling

CSS comes with a :optional and :required pseudo-class for the input, select, and textarea tag. The :optional pseudo-class represents an element that doesn’t have the required attribute set on it. The :required pseudo-class represents an element that does have the required attribute set on it.

```css
input:optional {
  border: 1px solid black;
}
input:required {
  border: 1px dashed red;
}
```

Credit: https://levelup.gitconnected.com/8-tricks-for-web-developers-you-can-put-into-practice-immediately-98079e65fd7d
