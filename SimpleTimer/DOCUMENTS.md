### Supported Commands :
* -s --start args:[duration=n hour/min/sec]
* -p --pause args:[timer_number=n]
* -r --resume args:[timer_number=n]
* -st --stop args:[timer_number=n]
* -ot --ongoing-timers args:none
* -sat --show-all-timers args:none
** Program will upgrade terminal and wait for any keystroke, then it will stop updating and goes right to terminal mode to get commands. If the user presses ESC, it will jump back to main page. 
** Database = [interval,interval,interval,...,interval], all interval types are integers
