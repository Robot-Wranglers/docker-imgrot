# This file describes terminal videos with the `vhs` tool (https://github.com/charmbracelet/vhs)
Output img/demo.gif 
Require "docker"
Set Shell "bash --norc --noprofile"
Set FontSize 16
Set Width 1200
Set Height 800
Set TypingSpeed .055
Set PlaybackSpeed 2
Set CursorBlink false
Type "# Demo!"
Enter
Enter
Sleep 3.3
Set PlaybackSpeed 3
Type "docker run --rm -v `pwd`:/workspace -w /workspace imgrot img/icon.png --range 360 --img-shape 200x200 --animate --display"
Sleep 2.8
Enter
Sleep 62

