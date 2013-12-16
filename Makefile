all:
	pyuic4 -o ui.py GUI/pyQtEpisoder.ui

clean:
	${RM} *.pyc
