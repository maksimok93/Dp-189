<h1>Practice</h1>
<h2>Task description</h2>
<p>Write a program which provides the statistic about given file. It has to print the following statistic about an<br>
arbitrary file:</p>
<ol>
<li>a number of lines</li>
<li>a number of empty lines</li>
<li>a number of lines with letter "z"</li>
<li>a number of "z" letters in the file</li>
<li>a number of lines with "and" group (for instance, "andromeda" has "and" as well as "you and me").</li>
</ol>
<p>Sample file (<code>./storage/run2019.txt</code>):</p>
<pre><code>zzzzzzzzz
zzz
zzzzzzzzzzzzzzzzzz

andromeda

and

z and a and z

</code></pre>
<p>Sample statistic:</p>
<pre><code>&gt;&gt;&gt;&gt;
File: ./storage/run2019.txt
  total lines:      10
  empty lines:      4
  lines with "z":   4
  "z" count":       34
  lines with "and": 3
&gt;&gt;&gt;&gt;
</code></pre>
<p>Please take into account, that the program</p>
<ul>
<li>has to ask a user about a path to a file</li>
<li>has to ask a user if one more file needs to be analyzed</li>
<li>has to stop only if a user wants to stop</li>
</ul>
