Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import sys
... if len(sys.argv) != 3:
...     print("Usage: python sum_args.py <num1> <num2>")
... else:
...     try:
...         num1 = int(sys.argv[1])
...         num2 = int(sys.argv[2])
...         total = num1 + num2
...         print("Sum =", total)
...     except ValueError:
