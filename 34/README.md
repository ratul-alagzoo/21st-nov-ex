Use the CPU and memory profilers discussed in the lecture (snakeviz, line_profiler, memray)
to analyze the sorting algorithms hosted at https://missing.csail.mit.edu/static/files/sorts.py.
Which algorithm “wins” in terms of run time, which in terms of memory consumption?


//cpu
open graphs:

uv run snakeviz <>.prof


//line graphs
Generate line profiles:

 uv run kernprof -l -v sorts_with_profiler.py
 
python -m line_profiler sorts_with_profiler.py.lprof

//memory profile
for each and every function 
 uv run memray run -o <func_name>.bin profile_memray.py 

