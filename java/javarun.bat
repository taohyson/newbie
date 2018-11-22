@ECHO OFF
CD /D %~dp1
IF EXIST target (
	DEL /Q /S target\*
	RMDIR /S /Q target
)
SETLOCAL ENABLEDELAYEDEXPANSION
SET FILES=
FOR %%I IN (*.java) DO (
	SET "FILES=!FILES! %%I"
)
javac -d target -encoding UTF-8 %FILES%
ECHO target\%~f1
IF EXIST target\%~f1.class (java target\%~f1)