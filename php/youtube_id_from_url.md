# Youtube id from URL

The script below can handle three common forms of YouTube URLS:
1. https://www.youtube.com/watch?v=kQbCf6A3uLY (default)
2. https://youtu.be/kQbCf6A3uLY (short URL, other extensions than .be also work)
3. https://www.youtube.com/embed/kQbCf6A3uLY (embed link)

```php
function get_youtube_id($url){
  if(strpos($url, "youtu") !== FALSE){
    // first, look for the video parameter v in the URL
    $parts = parse_url($url);
    parse_str($parts['query'], $query);
    if(isset($query['v'])){
      return $query['v'];
    }
    else{
      // second, the last segment of the url should hold the YouTube ID
      return end(explode("/",$parts[PHP_URL_PATH]));
    }
  }
  return null;
}
```
