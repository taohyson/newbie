@ECHO OFF

mkdir testdir
echo > testfile

COPY /A testfile testfile_copy
COPY /B testfile testfile_copy_EXE
COPY /D testfile testfile_copy_DECRP
COPY /Y testfile testfile_copy_NOTIP
COPY /Y testfile testdir

DEL /Q testfile* testdir\*
rmdir /s /q testdir