@ECHO OFF

ECHO HELLO WORLD! > TESTFILE
ECHO Pencil Sharpener >> TESTFILE
ECHO HELLO WORLD! >> TESTFILE
ECHO The scientists labeled their paper ""for discussion only."" It is not a final report. >> TESTFILE
ECHO hello world! >> TESTFILE

FIND "HELLO" TESTFILE
FIND /V "HELLO WORLD!" TESTFILE
FIND /C "HELLO WORLD!" TESTFILE
FIND /N "HELLO WORLD!" TESTFILE
FIND /I "HELLO WORLD!" TESTFILE
FIND "Pencil Sharpener" TESTFILE 
FIND "The scientists labeled their paper ""for discussion only."" It is not a final report." TESTFILE
FOR %%f IN (*.BAT) DO FIND "Pencil Sharpener" %%f
DIR /S /B . | FIND "FIND..BAT"

DEL TESTFILE 