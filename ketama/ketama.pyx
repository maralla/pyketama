import atexit

cdef extern from "ketama.h":
    ctypedef struct ketama_continuum:
        pass

    ctypedef struct mcs:
        unsigned int point
        char ip[22]

    int ketama_roll(ketama_continuum *contptr, char *filename)
    void ketama_smoke(ketama_continuum contptr)
    mcs* ketama_get_server(char*, ketama_continuum)
    void ketama_print_continuum(ketama_continuum c)
    char* ketama_error()


class KetamaError(Exception):
    pass


def _bytes(s):
    if isinstance(s, str):
        return s.encode("utf-8")
    return s

cdef class _Continuum:
    cdef public ketama_continuum _continum

    def __cinit__(self, filename):
        cdef ketama_continuum continum

        r = ketama_roll(&continum, <char*>filename)
        if not r:
            raise KetamaError(ketama_error().decode("ascii"))

        self._continum = continum

    def __dealloc__(self):
        ketama_smoke(self._continum)

    def get_server(self, k):
        cdef bytes key = _bytes(k)
        cdef mcs *mcsarr = ketama_get_server(<char*>key, self._continum)

        return mcsarr[0].point, mcsarr[0].ip

    def print_points(self):
        ketama_print_continuum(self._continum)


_continuum_map = {}

def create_continuum(filename):
    filename = _bytes(filename)
    if filename not in _continuum_map:
        _continuum_map[filename] = _Continuum(filename)
    return _continuum_map[filename]

atexit.register(lambda: _continuum_map.clear())
