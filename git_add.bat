@ECHO OFF

SET man1=%1

git add .
git rm --cached hiprovider\static\media\*.png
git rm --cached hiprovider\static\media\*.jpg

git status

git commit -m %man1%