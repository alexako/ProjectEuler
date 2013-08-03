ProjectEuler
============

Project Euler solutions in Python 2 www.projecteuler.net/
<br>


<h3>Progress Log</h3>

<h4>Problem 1</h4>
<ul>
    <li>Done! 1/21/2013</li>
    <li><a href="http://projecteuler.net/problem=1">projecteuler.net/problem=1</a></li>
    <li>Implemented list comprehension in sum() to find the sum of the multiples of 3 and 5 up to 1000</li>
</ul>

<h4>Problem 2</h4>
<ul>
    <li>Done! 1/21/2013</li>
    <li><a href="http://projecteuler.net/problem=2">projecteuler.net/problem=2</a></li>
    <li>Implemented common Fibonacci series generator</li>
</ul>

<h4>Problem 3</h4>
<ul>
    <li>Done! 1/22/2013</li>
    <li><a href="http://projecteuler.net/problem=3">projecteuler.net/problem=3</a></li>
    <li>Made one function to check if an int is prime</li>
    <li>Another function to find prime factors of a given int</li>
    <li>OverflowError solved by using the square root of the given int as the end of the range</li>
</ul>

<h4>Problem 4</h4>
<ul>
    <li>Done! 7/13/2013</li>
    <li><a href="http://projecteuler.net/problem=4">projecteuler.net/problem=4</a></li>
    <li>Used integers as strings to determine if the product was a palindrome.</li>
    <li>Decided to make the program scalable also by using integeres as strings (concatenated char zeroes)</li>
</ul>

<h4>Problem 5</h4>
<ul>
	<li>Done! 7/13/2013</li>
	<li><a href="http://projecteuler.net/problem=5">projecteuler.net/problem=5</a></li>
	<li>Took optimization advice from  <a href="http://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution">StackOverflow</a></li>
</ul>

<h4>Problem 6</h4>
<ul>
	<li>Done! 7/13/2013</li>
	<li><a href="http://projecteuler.net/problem=6">projecteuler.net/problem=6</a></li>
	<li>Too easy.</li>
</ul>

<h4>Problem 7</h4>
<ul>
	<li>Done! 7/13/2013</li>
	<li><a href="http://projecteuler.net/problem=7">projecteuler.net/problem=7</a></li>
	<li>Simple stuff. Used the same function from problem 3</li>
	<li>Added a counter and a while loop to find the nth prime number</li>
</ul>

<h4>Problem 8</h4>
<ul>
	<li>Done! 7/13/2013</li>
	<li><a href="http://projecteuler.net/problem=8">projecteuler.net/problem=8</a></li>
	<li>Converted thousand digit number into string in order to create a list of its digits</li>
	<li>Then simply made another list of sublists of five consecutive numbers incrementally</li>
	<li>Used operator module tip from <a href="http://stackoverflow.com/questions/2104782/returning-the-product-of-a-list">StackOverflow</a> to return a list of the products of each sublist</li>
</ul>

<h4>Problem 9</h4>
<ul>
	<li>Done! 7/13/2013</li>
	<li><a href="http://projecteuler.net/problem=9">projecteuler.net/problem=9</a></li>
	<li>Tried multiples of 3, 4, and 5; unsuccessful</li>
	<li>Resorted to Pythagorean Triples construct:</li>
	<ul>
		<li>Where n and m are any two positive integers (m &lt; n):</li>
		<li><a href="http://www.codecogs.com/eqnedit.php?latex=a&space;=&space;n^{2}&space;-&space;m^{2}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?a&space;=&space;n^{2}&space;-&space;m^{2}" title="a = n^{2} - m^{2}" /></a></li>
		<li><a href="http://www.codecogs.com/eqnedit.php?latex=b&space;=&space;2nm" target="_blank"><img src="http://latex.codecogs.com/gif.latex?b&space;=&space;2nm" title="b = 2nm" /></a></li>
		<li><a href="http://www.codecogs.com/eqnedit.php?latex=c&space;=&space;n^{2}&space;&plus;&space;m^{2}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?c&space;=&space;n^{2}&space;&plus;&space;m^{2}" title="c = n^{2} + m^{2}" /></a></li>
	</ul>
</ul>

<h4>Problem 10</h4>
<ul>
	<li>Done! 7/13/2013</li>
	<li><a href="http://projecteuler.net/problem=10">projecteuler.net/problem=10</a></li>
	<li>Used same fuctions from problem 3 and 7</li>
	<li>In is_prime(), I made the end of the range the square root of the given int to drastically speed up the program</li>
	<li>Earned 'Decathlete' award: completed 10 consecutive problems</li>
</ul>

<h4>Problem 11</h4>
<ul>
	<li>Done! 7/14/2013</li>
	<li><a href="http://projecteuler.net/problem=11">projecteuler.net/problem=11</a></li>
	<li>Turned in string into grid of integers</li>
	<li>Grouped factors into sublists of horizontal, vertical, diagonal left and right</li>
	<li>Changed range limits to fix index issues</li>
</ul>

<h4>Problem 12</h4>
<ul>
	<li>Done! 7/16/2013</li>
	<li><a href="http://projecteuler.net/problem=12">projecteuler.net/problem=12</a></li>
	<li>Need to optimize</li>
	<li>get_number_of_factors() is problematic</li>
	<li>Fixed! 7/16/2013</li>
	<li>Optimized by using xrange() instead of range() to reduce resource usage</li>
	<li>get_number_of_factors() refactored with advice from <a href= "http://codereview.stackexchange.com/questions/28527/simple-code-that-finds-number-of-factors-crashes-my-computer-is-there-a-workaro/28533?noredirect=1#28533">codereview.stackexchange.com</a></li>
</ul>

<h4>Problem 13</h4>
<ul>
    <li>Done! 7/19/2013</li>
    <li><a href="http://projecteuler.net/problem=13">projecteuler.net/problem=13</a></li>
    <li>Took a while to figure out what the problem was asking</li>
    <li>Fairly straight forward after figured that out</li>
    <li>Used list comprehension to get sum of the 50-digit numbers and printed the first ten digits</li>
</ul>

<h4>Problem 14</h4>
<ul>
    <li>Done! 7/20/2013</li>
    <li><a href="http://projecteuler.net/problem=14">projecteuler.net/problem=14</a></li>
    <li>Used a for loop to iterate the starting numbers and a while loop to find/count the chain</li>
    <li>Had an 'Off-by-one' error when counting the chain</li>
</ul>

<h4>Problem 15</h4>
<ul>
    <li>Done! 7/21/2013</li>
    <li><a href="http://projecteuler.net/problem=15">projecteuler.net/problem=15</a></li>
    <li>Used a horrific brute force method at first</li>
    <li>Problem most likely lies in the random generator of the next move</li>
    <li>With many, many trials and lots of brainstorming, I concluded that the total number of moves is equal to twice the size of the grid (20 Right, 20 Down)</li>
    <li>Left script running overnight and still no result</li>
    <li>After a bit of research in combinations and permutations, I found a formula for the total number of non-repeating combinations:</li>
        <ul>
            <li>Binomial Coefficient (where n is the number of things to choose from, and you choose r of them and repetition and order don't matter)</li>
            <li><img src="http://www.mathsisfun.com/combinatorics/images/combinations-no-repeat.png"></li>
            <li><a href="http://www.mathsisfun.com/combinatorics/combinations-permutations.html">Combinations and Permutations</a></li>
        </ul>
    <li>Implentation of formula and refactoring produced immensely faster results:</li>
        <ul>
            <li>Brute force method: inconclusive (runtime &gt; 10 hours)</li>
            <li>Binomial Coefficient: 0.002 seconds </li>
        </ul>
</ul>

<h4>Problem 16</h4>
<ul>
    <li>Done! 7/17/2013</li>
    <li><a href="http://projecteuler.net/problem=16">projecteuler.net/problem=16</a></li>
    <li>Another one-liner</li>
</ul>

<h4>Problem 17</h4>
<ul>
    <li>Done! 7/17/2013</li>
    <li><a href="http://projecteuler.net/problem=17">projecteuler.net/problem=17</a></li>
    <li>Could be done better. Mostly hardcoded.</li>
    <li>Used a dictionary to store number words</li> 
    <li>Used similar concept from problem 16</li>
</ul>

<h4>Problem 18</h4>
<ul>
    <li>Done! 7/31/2013</li>
    <li><a href="http://projecteuler.net/problem=18">projecteuler.net/problem=18</a></li>
    <li>Tried altering the algorithm from problem 17, but was inconclusive</li>
    <li>Tried a simpler approach. Start from the bottom and add the numbers upwards to ensure the highest possible sum</li>
    <li>Issue with comparing sums: iteration goes out of bounds</li>
    <li>[Fixed!] Made a seperate function, largest_sum(), to simplify things</li>
    <li>Got rid of the useless row size counter. Only made it more complicated.</li>
    <li>Used the same concepts in C++ solution</li>
</ul>

<h4>Problem 19</h4>
<ul>
    <li>Incomplete 8/1/2013</li>
    <li><a href="http://projecteuler.net/problem=19">projecteuler.net/problem=19</a></li>
    <li>In C++, stuck in infinite recursion</li>
    <li>Counter did not increment in recursion. Used pass-by-reference to fix</li>
    <li>In Python, tried a completely different approach. Still used same isLeapYear() function</li>
    <li>Seems more efficent, however it produces the wrong final answer.</li>
    <li>After 1911ish, off-by-one error somewhere</li>
    <li>[Fixed] But still produces an incorrect solution</li>
</ul>

<h4>Problem 20</h4>
<ul>
    <li>Done! 7/18/2013</li>
    <li><a href="http://projecteuler.net/problem=20">projecteuler.net/problem=20</a></li>
    <li>Pretty much straight forward</li>
    <li>Used the factorial formula given in problem description: n! = n * (n - 1)</li>
    <li>Turned the factorial into a string to get the sum of digits</li>
</ul>

<h4>Problem 25</h4>
<ul>
    <li>Done! 7/18/2013</li>
    <li><a href="http://projecteuler.net/problem=25">projecteuler.net/problem=25</a></li>
    <li>Used the same fibonacci series generator from  problem 2 with slight refactorization</li>
</ul>

<h4>Problem 29</h4>
<ul>
    <li>Done! 7/24/2013</li>
    <li>Completed in both Python and C++. Was a lot easier to code in Python</li>
    <li>Implemented recently learned concept of vectors (still not confident with them yet)</li>
</ul>

<h4>Problem 47</h4>
<ul>
    <li>Done! 7/24/2013</li>
    <li>Used a brute force method</li>
    <li>Fairly easy, however, limiting the range to the sqrt of num doesn't print the correct answer</li>
    <li>Could use a lot of optimization: runtime > 1500 seconds</li>
</ul>

<h4>Problem 48</h4>
<ul>
    <li>Done! 7/23/2013</li>
    <li>Another easy one</li>
    <li>Could have done a one-liner but opted for readability instead</li>
</ul>
