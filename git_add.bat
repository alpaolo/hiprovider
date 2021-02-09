@ECHO OFF

SET man1=%1

git add .
git rm --cached hiprovider\static\media\*.*

git status

git commit -m %man1%