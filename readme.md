# 📋 Content
Here you can find solution (on `python`) to **all** problems from 
[**[Yandex Training 3.0]**](https://yandex.ru/yaintern/algorithm-training)

## </> `template.py`
For convenience, You can use my `template.py`, in which you only need to change 
the `solve` function. It is designed not to care about input and output speed
(it is automatically done as fast as possible).
*Yes, in some tasks this is important...*

## 💫 "Tricks"

Top of my **conclusions** on this context:
- `input/output` is an indispensable part of the task; you need to think about how fast you read and write data; 
  that's what I wrote the `template.py`  to combat this problem (it is an adoptation
 of `@Slamur`s [**[template]**](https://github.com/Slamur/competitive-programming/blob/b20e338b3b3fe2f73c40cc2876e0520f4ac02ba8/course/templates/__Solution.py#L4))
 
- the problem's input limits are the most important information in the 
problem's condition; you can use them to figure out the asymptotic required 
solution (assume that `python` can handle `10^7` operations; 
then a `n * n` solution with an input complexity of `10 000` is not even
worth writing, while `n * logn` is fine)

- even simple arithmetic operations can be saved (for example, if suddenly
within a loop you repeatedly step to elements at some distance, for example 
`d * * 3`, then by storing this value at each iteration in the
`shift` variable, you can significantly speed up the program

* iterating over rows and columns in a matrix, if they are represented by a list
of lists, is not the same thing; (*yes, this is quite a basic rule,
but once in an asymptotically optimal solution I ran into this,
and for a long time I could not understand what solution the authors of the
problem expected from me...* the reason for this phenomenon is the physical 
arrangement of array memory elements and `random access` speed)
