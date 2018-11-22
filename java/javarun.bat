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
IF EXIST target\%~n1.class (
	cd target
	java %~n1
)