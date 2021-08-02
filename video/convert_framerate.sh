#fixing video woth wrong framerate (Obsbot)

mencoder -fps 60 -o NORM0001_60fps.MP4 -ovc copy -nosound NORM0001.MP4
