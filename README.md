ProjectEuler
============

Project Euler solutions in Python 2 www.projecteuler.net/

<h3>Progress Log</h3>

<h4>Problem 1</h4>
<ul>
    <li>Done! 1/21/2013</li>
    <li>Implemented list comprehension in sum() to find the sum of the multiples of 3 and 5 up to 1000</li>
</ul>

<h4>Problem 2</h4>
<ul>
    <li>Done! 1/21/2013</li>
    <li>Implemented common Fibonacci series generator</li>
</ul>

<h4>Problem 3</h4>
<ul>
    <li>Done! 1/22/2013</li>
    <li>Made one function to check if an int is prime</li>
    <li>Another function to find prime factors of a given int</li>
    <li>OverflowError solved by using the square root of the given int as the end of the range</li>
</ul>

<h4>Problem 4</h4>
<ul>
    <li>Done! 7/13/2013</li>
    <li>Used integers as strings to determine if the product was a palindrome.</li>
    <li>Decided to make the program scalable also by using integeres as strings (concatenated char zeroes)</li>
</ul>

<h4>Problem 5</h4>
<ul>
	<li>Done! 7/13/2013</li>
	<li>Took optimization advice from  <a href="http://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution">StackOverflow</a></li>
</ul>

<h4>Problem 6</h4>
<ul>
	<li>Done! 7/13/2013</li>
	<li>Too easy.</li>
</ul>

<h4>Problem 7</h4>
<ul>
	<li>Done! 7/13/2013</li>
	<li>Simple stuff. Used the same function from problem 3</li>
	<li>Added a counter and a while loop to find the nth prime number</li>
</ul>

<h4>Problem 8</h4>
<ul>
	<li>Done! 7/13/2013</li>
	<li>Converted thousand digit number into string in order to create a list of its digits</li>
	<li>Then simply made another list of sublists of five consecutive numbers incrementally</li>
	<li>Used operator module tip from <a href="http://stackoverflow.com/questions/2104782/returning-the-product-of-a-list">StackOverflow</a> to return a list of the products of each sublist</li>
</ul>

<h4>Problem 9</h4>
<ul>
	<li>Done! 7/13/2013</li>
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
	<li>Used same fuctions from problem 3 and 7</li>
	<li>In is_prime(), I made the end of the range the square root of the given int to drastically speed up the program</li>
	<li>Earned 'Decathlete' award: completed 10 consecutive problems</li>
</ul>

<h4>Problem 11</h4>
<ul>
	<li>Incomplete 7/13/2013</li>
	<li>Turned in string into grid of integers</li>
	<li>Grouped factors into sublists of horizontal, vertical, diagonal left and right</li>
</ul>
