Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> list1 = [1, 2, 3]
... list2 = [1, 2, 3]
... list3 = list1
... print("list1 == list2 :", list1 == list2)   # same content
... print("list1 is list2 :", list1 is list2)   # same object?
... print("list1 is list3 :", list1 is list3)   # same object?
... print("id(list1):", id(list1))
... print("id(list2):", id(list2))
