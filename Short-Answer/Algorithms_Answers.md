#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) -- the loop is dependent on n to happen

b) O(n^2) -- because there are nested for loops


c) O(n) -- the function runs n times


## Exercise II
  --I would solve this problem recursively, and I would start on the 0th floor. I would drop the egg from the 0th floor and check if its broken. If no, then I would gather my egg and move up to floor 1, where I would drop the egg and see if it is broken.

  I would keep doing this until I got to the floor where the egg broke. Then I would return what that floor is. This makes it an O(n) runtime complexity because it only recurses n number of times, whatever n may be.