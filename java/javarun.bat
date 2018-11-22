@echo off
cd %~dp1
if exist %~n1.class (
	del %~n1.class
)
javac -encoding UTF-8 %~nx1
if exist %~n1.class (
	java %~n1
)