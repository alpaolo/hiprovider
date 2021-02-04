@ECHO OFF

SET man1=%1

git add .

git status

git commit -m %man1%