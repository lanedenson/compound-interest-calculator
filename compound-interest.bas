1 rem variables
2 rem t = term of the investment
3 rem c = # of time compounded
4 rem p = principal
5 rem r = interest rate
6 rem u = times compounded
7 rem v = periodic interest rate
8 rem x = growth factor
9 rem y = compound growth factor
10 rem z = future value
11 print chr$(147) : rem clear the screen
20 print"*** compound interest calculator ***"
25 print
30 input"what is the starting amount"; p
35 print
40 input"what is the interest rate"; i
43 r=i/100
45 print
50 print"how long will this be invested"
55 input"(in years)"; t
58 print
60 print"how many time will this be compunded"
70 input"in a year"; c
75 print : print : print
80 print "great! let's walk through the math:" : print
85 print "****************************************"
90 u = c*t
100 print"this will be compounded";u;"times"
110 print"(";c;"times over the course of";t;"years)"
120 gosub 1000
130 v=r/c
140 print"the periodic interest rate is";v
145 print
150 print"(the interest rate:";i;"% divided by the"
160 print"number of times compounded:";c
170 gosub 1000
180 x=1+v
190 print"the growth factor is the periodic"
195 print"interest rate:";v;"plus 1"
197 print
200 print"for a total of";x
210 gosub 1000
220 y=x^u
225 print"the compound growth factor is the"
230 print"growth factor";x
233 print
235 print"raised to the power of the times"
240 print"compounded:";u
243 print
245 print "which equals";y
250 gosub 1000
255 z=y*p
260 print"finally, we calculate the total future"
270 print"value (including the initial investment)";
280 print"by multiplying the starting amount"
285 print"of $";p
287 print
290 print"by the compound growth factor:",y
295 print
300 print"for a total of $";z
310 gosub 1000
320 input"press y and enter to try again";again$
330 if again$="y" then goto 10
340 if again$<>"y" then print : print "goodbye!"
400 end
1000 rem **subr: pause&print blank line
1010 for l=1 to 3000:next
1020 print : print
1030 return
