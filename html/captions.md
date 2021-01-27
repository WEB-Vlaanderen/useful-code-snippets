# Captions or subtitles on videos and audo

Adding captions or subtitles to all the audio and video on your website helps your visitors a lot. That probably doesn't need any further explanation.
You can add a caption or subtitle by using the track tag. You can use this tag within the audio or video tag.

```html
<video controls src="/video.mp4">
    <track label="English" kind="subtitles" srclang="en" src="captions/video-en.vtt" default>
    <track label="Deutsch" kind="subtitles" srclang="de" src="captions/video-de.vtt">
    <track label="Español" kind="subtitles" srclang="es" src="captions/video-es.vtt">
</video>
```

The label attribute specifies the title of the text track. The kind attribute specifies the type of the text track and can have one of the following values: captions, chapters, descriptions, metadata, or subtitles. The srclang attribute specifies the language of the track text and is required if the kind attribute is subtitles.

Credit: https://levelup.gitconnected.com/8-tricks-for-web-developers-you-can-put-into-practice-immediately-98079e65fd7d
