<h1>Practice</h1>
<h2>Task description</h2>
<p>There is a decorator which measures execution time of decorated function</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> functools
<span class="pl-k">import</span> time

<span class="pl-k">def</span> <span class="pl-en">timer</span>(<span class="pl-smi">func</span>):
    <span class="pl-s"><span class="pl-pds">"""</span>Prints the runtime of the decorated function.<span class="pl-pds">"""</span></span>
    <span class="pl-en">@functools.wraps</span>(func)
    <span class="pl-k">def</span> <span class="pl-en">wrapper_timer</span>(<span class="pl-k">*</span><span class="pl-smi">args</span>, <span class="pl-k">**</span><span class="pl-smi">kwargs</span>):
        start_time <span class="pl-k">=</span> time.perf_counter()
        value <span class="pl-k">=</span> func(<span class="pl-k">*</span>args, <span class="pl-k">**</span>kwargs)
        end_time <span class="pl-k">=</span> time.perf_counter()
        run_time <span class="pl-k">=</span> end_time <span class="pl-k">-</span> start_time
        <span class="pl-c1">print</span>(<span class="pl-s">f</span><span class="pl-pds">"</span><span class="pl-s">Finished </span><span class="pl-c1">{</span>func.<span class="pl-c1">__name__</span><span class="pl-k">!r</span><span class="pl-c1">}</span><span class="pl-s"> in </span><span class="pl-c1">{</span>run_time<span class="pl-k">:.4f</span><span class="pl-c1">}</span><span class="pl-s"> secs</span><span class="pl-pds">"</span>)
        <span class="pl-k">return</span> value
    <span class="pl-k">return</span> wrapper_timer</pre></div>
<p>The current implementation will measure execution time only if a decorated function doesn't raise<br>
an error. But the current execution time won't be shown if some error will occur.</p>
<p>So, you need to update existing code in order to make it showing execution time regardless of<br>
errors in decorated function. And if an error happens, it has to be raised.</p>
<h2>Review items</h2>
<p>Please send a Python module for review which proves that updated decorator works regardless of<br>
errors in decorated function. The module should be executable using <code>python &lt;module&gt;.py</code>.</p>