import numpy
import matplotlib
import matplotlib.pyplot as plt

def gaussian(mu_x,sig_x,z):
	f = numpy.exp(-(z-mu_x)**2/(2 * sig_x**2))/(sig_x * numpy.sqrt(2*numpy.pi))
	return f

def battery(n):
    beta = 40
    a = 300
    b = 2000
    N = 10000
    X = numpy.zeros((N,1))
    for x in range(0, N):
        s = numpy.random.exponential(beta,n)
        X[x] = numpy.sum(s)


    mu_c = n * beta
    mu_t = beta
    sig_t = beta
    sig_c = beta * numpy.sqrt(n)
    nbins = 50
    edgecolor = 'w'
    bins = [float (x) for x in numpy.linspace(a,b,nbins+1)]
    h1, bin_edges = numpy.histogram(X, bins, density = True)

    be1 = bin_edges[0:numpy.size(bin_edges)-1]
    be2 = bin_edges[1:numpy.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0]
    plt.close('all')

    fig1 = plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor = edgecolor)

    plt.title('PDF of lifetime of a 24 batteries carton')
    plt.xlabel('Lifetime of a 24 batteries carton')
    plt.ylabel('PDF')
    f=gaussian(mu_c,sig_c,b1)
    plt.plot(b1,f,'r')

    fig2 = plt.figure(2)
    h2 = numpy.cumsum(h1)*barwidth
    plt.bar(b1,h2, width=barwidth, edgecolor = edgecolor)
    plt.title('CDF of lifetime of a 24 batteries carton')
    plt.xlabel('Lifetime of a 24 batteries carton')
    plt.ylabel('CDF')


battery(24)