import sympy as sp

def Derivative(f):
    x = sp.Symbol('x')
    f_expr = f(x)
    f_derivative = sp.diff(f_expr, x)
    return f_derivative

def evaluate(f, x1):
    x = sp.Symbol('x')
    return f.subs(x, x1)


def Newton_Raphson(f, a=0, b=0, eps=0.00000000001, max_iter=200):
    print("====================Newton Raphson starting...")
    i = 1
    xr = (a + b) / 2
    f_tag = Derivative(f)

    print("{:<10} {:<15} {:<15} {:<15}".format("Iteration", "xr", "f(xr)", "f'(xr)"))
    while abs(f(xr)) > eps and i < max_iter:
        f_xr = f(xr)
        f_tag_xr = evaluate(f_tag, xr)
        if f_tag_xr == 0:
            print("Derivative is zero. Cannot continue.")
            return

        tmp = xr - (f_xr / f_tag_xr)
        print("{:<10} {:<15} {:<15} {:<15}".format(i, xr, f_xr, f_tag_xr))
        xr = tmp
        i += 1

    if i == max_iter:
        print("Maximum iterations reached. No convergence.")
    else:
        print('\033[94m', f"\nThe equation f(x) has an approximate root at x = {xr}", '\033[0m')

def Secant_Method(f, a, b, eps=0.00000000001, max_iter=200):
    print("====================Secant Method starting...")
    i = 1
    xr0 = (a + b) * (1/3)
    xr1 = (a + b) * (2/3)

    print("{:<10} {:<15} {:<15} {:<15}".format("Iteration", "x(r)", "x(r+1)", "f(xr)"))
    while abs(f(xr0)) > eps and i < max_iter:
        f_xr0 = f(xr0)
        f_xr1 = f(xr1)
        f_tag_xr1 = (f_xr1 - f_xr0) / (xr1 - xr0)
        if f_tag_xr1 == 0:
            print("Derivative is zero. Cannot continue.")
            return
        tmp = xr1 - (f_xr1 / f_tag_xr1)
        print("{:<10} {:<15} {:<15} {:<15}".format(i, xr0, xr1, f_xr1))
        xr0=xr1
        xr1=tmp
        i += 1

    if i == max_iter:
        print("Maximum iterations reached. No convergence.")
    else:
        print('\033[94m', f"\nThe equation f(x) has an approximate root at x = {xr0}", '\033[0m')


# Main program
if __name__ == '__main__':
    Newton_Raphson(lambda x: 4*x ** 3 - 48*x + 5, 3, 4)
    Secant_Method(lambda x: 4 * x ** 3 - 48 * x + 5, 3, 4)