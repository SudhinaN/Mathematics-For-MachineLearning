
# PACKAGE
# Here are the imports again, just in case you need them.
# There is no need to edit or submit this cell.
import numpy as np
import numpy.linalg as la
# from readonly.PageRankFunctions import *
np.set_printoptions(suppress=True)
# GRADED FUNCTION
# Complete this function to provide the PageRank for an arbitrarily sized internet.
# I.e. the principal eigenvector of the damped system, using the power iteration method.
# (Normalisation doesn't matter here)
# The functions inputs are the linkMatrix, and d the damping parameter - as defined in this worksheet.
def pageRank(linkMatrix, d):
    n = linkMatrix.shape[0]
    r = 100 * np.ones(n) / n  # Sets up this vector (6 entries of 1/6 × 100 each)
    M = d * linkMatrix + (1 - d) / n * np.ones([n, n])
    lastR = r
    r = M @ r
    i = 0
    while la.norm(lastR - r) > 0.01:
        lastR = r
        r = M @ r
        i += 1
    print(str(i) + " iterations to convergence.")
    r
    return r




linkmatrix = np.array([[0, 1 / 2, 1 / 3, 0, 0, 0, 0],
                       [1 / 3, 0, 0, 0, 1 / 2, 0, 0],
                       [1 / 3, 1 / 2, 0, 1, 0, 1 / 3, 0],
                       [1 / 3, 0, 1 / 3, 0, 1 / 2, 1 / 3, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1 / 3, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1 / 3, 1]])
print(pageRank(linkmatrix, 0.1))

# PACKAGE
# Here are the imports again, just in case you need them.
# There is no need to edit or submit this cell.
# import numpy as np
# import numpy.linalg as la
# from readonly.PageRankFunctions import *
#
# np.set_printoptions(suppress=True)


# # GRADED FUNCTION
# # Complete this function to provide the PageRank for an arbitrarily sized internet.
# # I.e. the principal eigenvector of the damped system, using the power iteration method.
# # (Normalisation doesn't matter here)
# # The functions inputs are the linkMatrix, and d the damping parameter - as defined in this worksheet.
# def pageRank(linkMatrix, d):
#     eVals, eVecs = np.la.eig(linkmatrix)  # Gets the eigenvalues and vectors
#     order = np.absolute(eVals).argsort()[::-1]  # Orders them by their eigenvalues
#     eVals = eVals[order]
#     eVecs = eVecs[:, order]
#
#     r = eVecs[:, 0]  # Sets r to be the principal eigenvector
#     100 * np.real(r / np.sum(r))  # Make this eigenvector sum to one, then multiply by 100 Procrastinating Pats
#
#     linkmatrix = np.array([[0, 1 / 2, 1 / 3, 0, 0, 0, 0],
#                            [1 / 3, 0, 0, 0, 1 / 2, 0, 0],
#                            [1 / 3, 1 / 2, 0, 1, 0, 1 / 3, 0],
#                            [1 / 3, 0, 1 / 3, 0, 1 / 2, 1 / 3, 0],
#                            [0, 0, 0, 0, 0, 0, 0],
#                            [0, 0, 1 / 3, 0, 0, 0, 0],
#                            [0, 0, 0, 0, 0, 1 / 3, 1]])
#     pageRank(linkmatrix, pages)
#
#     return r
