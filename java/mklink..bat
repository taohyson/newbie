@ECHO OFF

MKLINK %JAVA_HOME%\bin\JAVARUN.BAT JAVARUN.BAT
MKLINK java.sublime-build "C:\Users\zx\AppData\Roaming\Sublime Text 3\Packages\User\java.sublime-build"

DIR java.sublime-build
TYPE java.sublime-build