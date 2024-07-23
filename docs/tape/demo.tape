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
Type "python demo.py img/icon.png --display"
Sleep 2.8
Enter
Sleep 30

