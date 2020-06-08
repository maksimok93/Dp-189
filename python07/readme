<h1>Practice</h1>
<h2>Task description</h2>
<p>Write a program which filters a given file or annotates its lines with relevant rules. It should<br>
run like</p>
<div class="highlight highlight-source-shell"><pre>python -m silters (filter <span class="pl-k">|</span> annotate) <span class="pl-k">&lt;</span>a file path<span class="pl-k">&gt;</span></pre></div>
<p>If <code>filter</code> option is requested, the program should display lines based on rules below. If<br>
<code>annotate</code> option is requested, the program has to display the information about which rules are<br>
applicable for each line using <code>&lt;line number&gt;: [rule] ...</code> format. For instance, like this</p>
<pre lang="text"><code>1: FP001
2:
3: FP001 FP002 FN203
4: FN203
</code></pre>
<p>There are the following rules for the content:</p>
<ul>
<li>display a line if it
<ul>
<li>ends with a dot (FP001)</li>
<li>is less than 100 characters (FP002)</li>
<li>has at least 5 <code>a</code> letters (FP003)</li>
</ul>
</li>
<li>don't display a line if it
<ul>
<li>has more than 3 <code>z</code> letters (FN201)</li>
<li>is an empty line (FN202)</li>
<li>consists only from non-letter characters (FN203)</li>
</ul>
</li>
</ul>
<p>The "display" rules have a priority over the "non-display" rules. For instance, if there is a line<br>
like <code>zaz zara Ararat ZULU Ozz and more amazing words</code>, it should be printed.</p>
<p>Also, each rule has to be implemented by extending the following abstraction</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> abc <span class="pl-k">import</span> <span class="pl-c1">ABC</span>, abstractmethod


<span class="pl-k">class</span> <span class="pl-en">Filter</span>(<span class="pl-c1">ABC</span>):
    <span class="pl-en">@abstractmethod</span>
    <span class="pl-k">def</span> <span class="pl-en">name</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>) -&gt; <span class="pl-c1">str</span>:
        <span class="pl-s"><span class="pl-pds">"""</span>Provides a name of the rule (like FP005).<span class="pl-pds">"""</span></span>
        <span class="pl-k">pass</span>
    
    <span class="pl-en">@abstractmethod</span>
    <span class="pl-k">def</span> <span class="pl-en">matches</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">line</span>: <span class="pl-c1">str</span>) -&gt; <span class="pl-c1">bool</span>:
        <span class="pl-s"><span class="pl-pds">"""</span>Returns True if a given line matches the filter, otherwise, returns False.<span class="pl-pds">"""</span></span>
        <span class="pl-k">pass</span></pre></div>
<p>Also, try to create an abstraction to express different options (we have <code>filter</code> and <code>annotate</code>)<br>
now. And don't forget to apply other OOD design approaches if any. Ideally, the implementation<br>
should have no functions, only classes.</p>
<h2>Review items</h2>