import numpy


def multiply_diagonal_v(x):
    return numpy.prod(numpy.diag(x)[numpy.diag(x) != 0])


def equal_multiset_v(x, y):
    return numpy.array_equal(numpy.sort(x), numpy.sort(y))


def max_before_zero_v(x):
    return numpy.max(x[1:][(x == 0)[:-1]])

def convert_image(img, coefs):
    return numpy.dot(img, coefs).astype(numpy.uint8)


def pair_distance(x, y):
    return numpy.sqrt(numpy.sum((x[:, numpy.newaxis] - y) ** 2, axis=-1))


def run_length_encoding(x):
    if x.size == 0:
        return numpy.array([]), numpy.array([])
    n = numpy.concatenate(([0], numpy.where(x[:-1] != x[1:])[0] + 1))
    m = numpy.diff(numpy.concatenate((n, [x.size])))
    return x[n], m

