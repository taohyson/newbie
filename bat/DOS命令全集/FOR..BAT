@ECHO OFF
rem FOR /?

MKDIR TESTDIR
COPY /A /Y *.BAT TESTDIR
ECHO MILK,CAFFEE,TEA,WATER; > TESTFILE

FOR %%I IN (*) DO ECHO %%I
FOR /D %%I IN (*) DO ECHO :	%%I
FOR /R . %%I IN (*) DO ECHO :			%%I
FOR /L %%I IN (5,-1,1) DO ECHO %%I
FOR /F "eol=; tokens=2,3* delims=, " %%I IN (TESTFILE) DO @ECHO %%I %%J %%K
FOR /F "eol=; tokens=2,3* delims=, " %%I IN ("CAT,DOG,COW,PIG;") DO @ECHO %%I %%J %%K
FOR /F "eol=; tokens=1,2 delims== " %%I IN ('SET') DO @ECHO %%I %%J

DEL /Q TESTFILE
RMDIR /S /Q TESTDIR