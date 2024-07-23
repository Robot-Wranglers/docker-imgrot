# This file describes terminal videos with the `vhs` tool 
# See https://github.com/charmbracelet/vhs for docs
Output img/demo.chafa.gif 
Require "docker"
Set Shell "sh"
Set FontSize 16
Set Width 700
Set Height 500
Set TypingSpeed .06
Set PlaybackSpeed 1
Set CursorBlink false
Type "docker run -it --rm -v `pwd`:/workspace -w /workspace robotwranglers/imgrot img/icon.png --range 360 --img-shape 200x200 --display"
Sleep 2.2
Enter
Sleep 30

