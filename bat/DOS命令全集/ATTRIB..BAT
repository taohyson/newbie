@ECHO OFF

ATTRIB TESTFILE
ATTRIB TESTFILE +A +R +S +H
ATTRIB TESTFILE

ATTRIB TESTDIR
ATTRIB TESTDIR +A +R +S +H /S /D
ATTRIB TESTDIR