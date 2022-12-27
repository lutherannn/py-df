# Deadfish compiler, and ASCII codes back into Deadfish
Why are you even looking at this, it isn't useful. Go do something more productive like working out or touching grass. This is merely my cry for help<br>

# Tests
asc.out is the output after running ascii-interpret.asc on ascii-interpreter.py<br>
ascii-interpret.asc is the input file for ascii-interpreter.py. It contains ASCII keywords, one on each line<br>
helloworld.df is a hello world program written in deadfish. I'm not sure if that's the shortest way to do it or not<br>

# Usage
ascii-interpreter.py \<inputfile\> \<outputfile\><br>
df-interpreter.py \<inputfile\><br>

# Basics of Deadfish:
It's basically brainfuck without loops, and only working on one cell at a time, which makes it super easy to do something like this.<br>
It has four, idk, commands? i, d, s, o.<br>
i increases the count of the current cell by one<br>
d decreases the count of the current cell by one<br>
s squares the current cell<br>
o outputs the cell<br>

so, for example, the ascii code for a newline is 10. In Deadfish that would be:<br>
iiisio<br>
three i's make the cell 3, the s squares the s to 9, the i adds one more to make it 10, and the o outputs it.<br>

# Limitations
Currently, you can't put a comment on the end of a line in your Deadfish input, since it only skips the line if it starts with a pound sign.<br>
However, you can put whatever you want in an uncommented line, as long as it doesn't contain a lowercase i, d, s, or o. You'll see in my hello world I tried my best to make it readable.<br>

# TODO
Finish adding the ASCII codes to ascii.py, and add useful functions<br>

life is but a stream~
