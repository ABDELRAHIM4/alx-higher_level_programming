#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
    if (PyList_Check(p)) {
        printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
        printf("[*] Allocated = %ld\n", PyList_GET_SIZE(p));

        for (Py_ssize_t i = 0; i < PyList_GET_SIZE(p); i++) {
            PyObject *element = PyList_GET_ITEM(p, i);

            if (PyUnicode_Check(element)) {
                printf("Element %ld: str\n", i);
            } else if (PyLong_Check(element)) {
                printf("Element %ld: int\n", i);
            } else if (PyFloat_Check(element)) {
                printf("Element %ld: float\n", i);
            } else if (PyTuple_Check(element)) {
                printf("Element %ld: tuple\n", i);
            } else if (PyList_Check(element)) {
                printf("Element %ld: list\n", i);
            } else {
                printf("Element %ld: unknown\n", i);
            }
        }
    } else {
        printf("Object is not a Python List\n");
    }
}
