# External links

If you want to style all external links on your website (e.g. yourwebsite.com), you can use the CSS code below.

```css
a[href*="//"]:not([href*="yourwebsite.com"]) {
  /* Apply style here */
}
```

You can also add an icon to an external link using the snippet below

``` 
a[href*="//"]:not([href*="yourwebsite.com"])::after {
  content: '(external link)';
  display: inline-block;
  width: .7em;
  height: .7em;
  text-indent: .7em;
  white-space: nowrap;
  overflow: hidden;
  background-image: url('https://upload.wikimedia.org/wikipedia/commons/4/44/Icon_External_Link.svg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100%;
  margin-left: .1em;
}
```

Credit: 
- https://levelup.gitconnected.com/8-tricks-for-web-developers-you-can-put-into-practice-immediately-98079e65fd7d
- https://codepen.io/simevidas/pen/MKdmeV?editors=0110
