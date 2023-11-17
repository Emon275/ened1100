from math import *
# the math import above is to allow you to input methods from the math module such as sqrt().



# This is the main class of the whole module.
#  It takes the basic inputs for integration and also puts functions into their correct form so that python can read well.
#  Through inheritance, it works with other classes.


class Integration:
    def __init__(self, f, variable, lower, upper):
        self.f = f
        self.variable = variable
        self.lower = lower
        self.upper = upper

    def correct_input_form(self):
        function_to_return = ''
        
        if "^" in self.f:

            self.f = self.f.replace("^", "**")

        for i in range(len(self.f)):

            try:
                if i > 0 and ((self.f[i] == self.variable and isinstance(int(self.f[i-1]), int)) or (self.f[i] == "(" and isinstance(int(self.f[i-1]), int))):
                    function_to_return += "*"
            except ValueError:
                pass
            finally:
                function_to_return += self.f[i]
        function_to_return = function_to_return.replace(self.variable, 'x')
        self.f = function_to_return


class Reimann(Integration):

    def __init__(self, f, variable, lower, upper, n):
        super().__init__(f, variable, lower, upper)
        self.correct_input_form()
        self.n = n

    # Riemanns Sum
    def right_riemann(self):

        width = (self.upper - self.lower) / (self.n * 1.0)

        f = 0
        for i in range(1, self.n + 1):
            x = self.lower + i * width
            f += eval(self.f)
        size = f * width
        print(round(size, 4))

    def left_riemann(self):

        width = (self.upper - self.lower) / (self.n * 1.0)
        f = 0
        for i in range(self.n):
            x = self.lower + i * width
            f += eval(self.f)
        size = f * width
        print(round(size, 4))


    def upper_riemann(self):

        width = (self.upper - self.lower) / (self.n * 1.0)

        f = 0
        for i in range(1, self.n + 1):
            x = self.lower + i * width
            g = eval(self.f)
            x = self.lower + (i - 1) * width
            h = eval(self.f)
            if g > h:
                f += g
            else:
                f += h
        size = f * width
        print(round(size, 4))

    def lower_riemann(self):

        width = (self.upper - self.lower) / (self.n * 1.0)
        f = 0
        for i in range(1, self.n + 1):
            x = self.lower + i * width
            g = eval(self.f)
            x = self.lower + (i - 1) * width
            h = eval(self.f)
            if g < h:
                f += g
            else:
                f += h
        size = f * width
        print(round(size, 4))

    def mid_riemann(self):

        width = (self.upper - self.lower) / (self.n * 1.0)

        f = 0
        for i in range(1, self.n + 1):
            x = self.lower + i * width
            g = eval(self.f)
            x = self.lower + (i - 1) * width
            h = eval(self.f)

            f += ((g + h) / 2)
        size = f * width
        print(round(size, 4))


# Reimann("2x+3", 'x', 1, 4, 4).left_riemann()


##----------------------------------This is the end of the riemann class-------------------------------

## ---------------------------------Trapezium class -------------------------------------------------

# So this is the trapezium. It inherits from the Integration class and works normally like the way normal trapezium rule works
# Even though i still have a little problem with the trapezium rule, i think this is ok.
# Works well. Tested it quite a couple of times

class Trapezium(Integration):
    Area = 0

    def __init__(self, f, variable, lower, upper, n):
        super(Trapezium, self).__init__(f, variable, lower, upper)
        self.correct_input_form()
        self.n = n

    def trapezium(self):
        area = 0

        change_in_limit = (self.upper - self.lower)/self.n

        for i in range(self.n+1):
            x = self.lower + change_in_limit * i

            if x != self.lower and x != self.upper:

                area += 2*eval(self.f)
                continue

            area += eval(self.f)

        Trapezium.Area = 0.5 * change_in_limit *area
        print(Trapezium.Area)
        return Trapezium.Area

##-----------------------------------------End of the trapezium class ----------------------------------

## ------------------------------------------- Simpson's rule -------------------------------------------

# So this is the simpson class. Works works with the two types of simpson's rule

class Simpson(Integration):
    Area = 0

    def __init__(self, f, variable, lower, upper, n):
        super().__init__(f, variable, lower, upper)
        self.correct_input_form()
        self.n = n

    def simpson_even(self):
        area = 0
        change_in_limit = (self.upper - self.lower) / self.n

        for i in range(self.n + 1):
            x = self.lower + change_in_limit * i

            if x != self.lower and x != self.upper:
                if i % 2 == 1:
                    area += 4 * eval(self.f)
                else:
                    area += 2 * eval(self.f)
                continue

            area += eval(self.f)


        Simpson.Area = 1/3 * change_in_limit * area
        print(Simpson.Area)

    def simpson_odd(self):
        area = 0
        change_in_limit = (self.upper - self.lower) / self.n

        for i in range(self.n + 1):
            x = self.lower + change_in_limit * i

            if x != self.lower and x != self.upper:
                if i % 3 == 0:
                    area += 2 * eval(self.f)

                else:
                    area += 3 * eval(self.f)

                continue

            area += eval(self.f)

        Simpson.Area = 3/8 * change_in_limit * area
        print(Simpson.Area)

    def simpson_run(self):
        if self.n % 2 == 0:
            self.simpson_even()
        else:
            self.simpson_odd()
## ------------------------------------------- End of Simpson's rule -------------------------------------------

##  -------------------------------------------Romberg rule -------------------------------------------

# NO problem with this but just that its very accurate hence could exactly test it with the once we have done in class so far

class Romberg(Trapezium):

    def __init__(self, f, variable, lower, upper, n):
        super().__init__(f, variable, lower, upper, n)
        self.sweep = n
        self.rectangles = [2**x for x in range(n)]
        self.trapezium_n = []
        self.richalison_n = []
        self.romberg_n = {}

    def trapeziums(self):
        for i in self.rectangles:
            self.n = i
            self.trapezium_n.append(self.trapezium())

    def richalison(self):
        self.richalison_n = [self.trapezium_n[i]-(self.trapezium_n[i] - self.trapezium_n[i-1])/3 for i in range(len(self.trapezium_n)) if i>0]


    def romberg(self):
        order_of_iteration = 1
        sweep = 1

        for i in range(1, self.sweep+1):
            self.romberg_n.setdefault(i, {})

        for i in self.trapezium_n:

            self.romberg_n[order_of_iteration][sweep] = i
            sweep += 1

        order_of_iteration = 2
        sweep = 2
        for i in self.richalison_n:
            self.romberg_n[order_of_iteration][sweep] = i
            sweep += 1

        order_of_iteration = 3
        sweep = 3

        while len(self.romberg_n[order_of_iteration-1])>1:

            for i in range(len(self.romberg_n[order_of_iteration-1])-1):

                i = self.romberg_n[order_of_iteration-1][sweep] + (self.romberg_n[order_of_iteration-1][sweep] - self.romberg_n[order_of_iteration-1][sweep-1])/((4**(order_of_iteration-1)) - 1)
                self.romberg_n[order_of_iteration][sweep] = i

                sweep += 1

            order_of_iteration += 1
            sweep = order_of_iteration

        #print(self.romberg_n)
        print("Romberg :", self.romberg_n[order_of_iteration-1][sweep-1])
## -------------------------------------------End of Romberg's rule -------------------------------------------

## Tested code.
# But if you think you can not do you part and think school is going to hinder you, let me know.
# i want to make sure that i finish this before vacation even if school work hinders me. i don't know of you
#By the way, sorry for my poor programming skills, i'm still improving on it. Please don't laugh at me.


# the parameters are (the function, the variable for the equation or function, lower limit, upper limit, n or the number of rectangles or whatever n is depending on that you are solving)
# this is to give you headstart on how to understand what i have done below
a = Romberg("0.2 + 25x -200x^2 + 675x^3 - 900x^4 + 400x^5", "x", 0, 0.8, 4)
a.trapeziums()
a.richalison()
a.romberg()

b = Simpson("0.2 + 25x -200x^2 + 675x^3 - 900x^4 + 400x^5", "x", 0, 0.8, 4)
b.simpson_run()

c = Trapezium("0.2 + 25x -200x^2 + 675x^3 - 900x^4 + 400x^5", "x", 0, 0.8, 4)
c.trapezium()

d = Reimann("0.2 + 25x -200x^2 + 675x^3 - 900x^4 + 400x^5", "x", 0, 0.8, 4)
d.right_riemann()

## ----------------------------------------- Concluding notes ----------------------------------------------

# If you have any issue at all lemme know. Especially with the programming

####### See you later, Christopher

"__authors__" == "Christopher and Hannah"