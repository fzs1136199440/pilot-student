# p2-1-function-def



### **函数和变量的命名规则**

> 哪怕一个函数什么也不干，它也必须得有一个名字，名字后面必须加一个`()`，以表明它是一个函数，而不是某个变量。

+ 首先，名称**只能**以大小写字母或者下划线`_`开头，其它的任何东西都不行（如数字、特殊符号等）;
+ 其次，名称中**不能有空格**，如果一个名称中有几个词汇，可以**用下划线分隔开**（如`do_nothing`），也可以用Camel Case（如`doNothing`），但更推荐下划线，因为下划线的分隔更明显，更利于阅读；
+ 最后，**绝对不能**与Python语言的**关键字**（keyword，关键字也叫**保留字**reserved）重复。



### **函数的状态**

#### **参数**：

+ 没有参数的状态下，意味着这个函数的执行**不依赖于参数输入**。
+ 有一个或多个参数的状态下，函数调用时输入参数的值是严格按照**参数顺序**去匹配的。

#### **返回值**：

+ 没有返回值的状态下，是因为其函数内部不存在由`return`引导的返回语句。
+ 有一个或多个返回值，这是大多数情境下的使用，因为多数情况下要做数据处理，要从输入得到输出。返回值也是按顺序返回的，当返回值需要赋值给变量时，也要按顺序来。



### **函数内与函数外：变量的作用域**

```py
def increase_one(n):
	n += 1
	return n
	
n = 1
print(increase_one(n)) # 返回值为 2.
print(n) # 返回值为 1.
```

为什么这段代码里的两个`print()`函数输出分别是 2 和 1。

这要涉及到概念**变量的作用域**，也就是说在不同地方出现的同名变量和函数，可能是完全不同的两个东西：

+ 函数定义体中的变量的作用域是在该函数内部，程序的其他部分不知道其存在，这种变量叫**局部变量**（local variable）；函数的输入参数也是局部变量，也只在函数定义体中有效；
+ 不在任何函数、类定义中的变量的作用域是全局的，在任何地方都可以访问，这种变量称为**全局变量**；
+ 如果局部变量和全局变量同名，函数定义体内会优先局部变量，不会把他它当做全局变量。

这样我们就能理解上面代码输出的 2 和 1 了：

- 第一个`print()`打印的是函数调用`increase_one(n)`的返回值，这个语句不在任何函数定义体中，所以它里面用到的变量都是全局变量：
  - 在调用 `increase_one()` 时参数 `n`，按照作用域原理，是全局变量 `n` 当时的值，也就是 1；
  - 在 `increase_one()` 函数定义内，参数 `n` 是输入参数即局部变量，带着传进来的值 1，经过加一之后返回，返回值是 2；
  - `print` 打印这个返回值，输出 2；
  - 这个过程中处理的都是局部变量，完全不影响全局变量 `n` 的值；
- 第二个 `print()` 打印的是全局变量 `n` 的值，输出出 1。

