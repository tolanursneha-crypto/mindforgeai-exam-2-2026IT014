# Explanation

* The function accepts attendance percentage, diary entries, and tasks completed as input.

* It calculates a readiness score out of 100.

* It uses if-elif conditions:
   1. If attendance is below 50%, 10 marks are deducted.
   2. If attendance is 90% or above and tasks completed are 8 or more, 5 bonus marks are added.
   
* The final score is always kept between 0 and 100 using max() and min().