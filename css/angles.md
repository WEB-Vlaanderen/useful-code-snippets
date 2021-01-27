# Using angles in CSS

Angles get used a lot in CSS to rotate a certain element or to create an animation. Most of the time we use something like transform: rotate(180deg) for this. But there are several other possible units that you could use here. You can also use rad, grad, and turn.
The most interesting one is the turn unit. Instead of writing transform: rotate(180deg) you could also use transform: rotate(0.5turn). Or if you want to rotate an element two times you could use transform: rotate(2turn) instead of transform: rotate(720deg).

```css
.some-class{
    transform: rotate(0.5turn) /* 180 degrees (upside down) */
}
```

Credit: https://levelup.gitconnected.com/8-tricks-for-web-developers-you-can-put-into-practice-immediately-98079e65fd7d
