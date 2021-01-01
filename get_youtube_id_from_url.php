<?php
function get_youtube_id($url){
  if(strpos($url, "youtu") !== FALSE){
    $parts = parse_url($url);
    parse_str($parts['query'], $query);
    if(isset($query['v'])){
      return $query['v'];
    }
    else{
      return end(explode("/",$parts[PHP_URL_PATH]));
    }
  }
  return null;
}
?>
