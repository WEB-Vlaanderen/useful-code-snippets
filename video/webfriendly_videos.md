To make sure your video can be played in most browsers, make sure you include your video in multiple formats.
The example belows shows how a video can be included with autoplay, loop and no controls.

```html
<video poster="output.jpg" preload="auto" style="pointer-events: none;display: block;" autoplay loop muted playsinline>
  <source src="output.mp4" type="video/mp4">
  <source src="output.ogv" type="video/ogg">
  <source src="output.webm" type="video/webm">
  Your browser does not support the video tag.
</video>
```

To obtain all assets you need to create a video <input>, e.g. input.mp4 and run the commands below:

```bash
ffmpeg -i <input> -c:v libtheora -q:v 7 -c:a libvorbis output.ogv
ffmpeg -i <input> -c:v libvpx-vp9 -crf 30 -b:v 0 output.webm
ffmpeg -i <input> -c:v libx264 -crf 23 -b:v 0 output.mp4

ffmpeg -i <input> -vframes 1 output.jpg
```


