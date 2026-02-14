static int list_append(PyListObject *self, PyObject *v)
{
    if (self->allocated <= Py_SIZE(self)) {
        if (list_resize(self, more) == -1)
            return -1;
    }
    Py_INCREF(v);
    Py_SET_SIZE(self, Py_SIZE(self)+1);
    PyList_SET_ITEM(self, Py_SIZE(self)-1, v);
    return 0;
}