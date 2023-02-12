set PYTHON_EXE_311=%USERPROFILE%\AppData\Local\Programs\Python\Python311\python.exe
set PYTHON_EXE_310=%USERPROFILE%\AppData\Local\Programs\Python\Python310\python.exe
set PYTHON_EXE_39=%USERPROFILE%\AppData\Local\Programs\Python\Python39\python.exe
set PYTHON_EXE_39=%USERPROFILE%\AppData\Local\Programs\Python\Python38\python.exe

if exist %PYTHON_EXE_311% (
  start %PYTHON_EXE_311% .\pokerok_to_pokerstars.py
) else if exist %PYTHON_EXE_310% (
  start %PYTHON_EXE_310% .\pokerok_to_pokerstars.py
) else if exist %PYTHON_EXE_39% (
  start %PYTHON_EXE_39% .\pokerok_to_pokerstars.py
) else (
  echo Error: Python 3.11, 3.10 or 3.9 not found.
)

exit
