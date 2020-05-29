<h1>Practice</h1>
<h2>Task description</h2>
<p>Please write a program which calculates project estimates using <a href="https://en.wikipedia.org/wiki/Three-point_estimation" rel="nofollow">https://en.wikipedia.org/wiki/Three-point_estimation</a>.<br>
It asks a user for providing available tasks (at least one) with 3 required estimates (<code>a</code>, <code>m</code>, <code>b</code>). After, it<br>
calculates an estimate (E) and a standard deviation (SD) for each task using the following formulae:</p>
<pre lang="text"><code>E(task) = (a + 4m + b) / 6
SD(task) = (b − a) / 6
</code></pre>
<p>Finally, it calculates the 95% confidence interval (CI) for the project based on<br>
<a href="https://en.wikipedia.org/wiki/Three-point_estimation#Project_management" rel="nofollow">https://en.wikipedia.org/wiki/Three-point_estimation#Project_management</a>. It means that <code>E(project)</code> and <code>SE (project)</code> (<code>SE(task)</code> is equal to <code>SD(task)</code> above) have to be calculated before making the final evaluation of<br>
<code>CI(project) = E(project) ± 2 × SE(project)</code>. The final values have to be printed like:</p>
<pre lang="text"><code>Project's 95% confidence interval: 100 ... 120 points
</code></pre>
<p>where <code>100</code> and <code>120</code> are values of Min and Max <code>CI(project)</code>.</p>
<h2>Review items</h2>
<p>Please send <code>.zip</code> archive of the project along with usage instructions.</p>