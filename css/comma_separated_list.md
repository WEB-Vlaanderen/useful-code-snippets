# Create a comma separated list using ul > li and CSS

Here is a neat little trick that allows you to create a comma-separated list using just an HTML unordered list and a couple of lines of CSS.

```css
ul > li:not(:last-child):after { 
  content: “, “; 
}
```

In order for this to work you need to make sure to set the display property of the li tag to inline-block.

```html
<ul>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ul>
```

This is what the result looks like:

```
First item, Second item, Third item
```

Credit: https://levelup.gitconnected.com/8-tricks-for-web-developers-you-can-put-into-practice-immediately-98079e65fd7d
