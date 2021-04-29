import numpy as np
import pymanopt as pm
import scipy.linalg as la
import autograd.numpy as anp
import pymanopt.solvers as solvers
import autograd.numpy.linalg as ala
import pymanopt.manifolds as manifolds
from sklearn.preprocessing import scale
from sklearn.metrics import pairwise_distances

class JDIP:

    def __init__(self,dimension=30,lamda=1e-5,sigma=None,maxiter=5,verbosity=0):
        """

        """        
        args_values = locals()
        args_values.pop("self")
        for arg,value in args_values.items():
            setattr(self,arg,value)
    
    def fit(self,Xs,ys,Xt,yt,Ws=None,Wt=None):
        """
        
        """
        ns,dim = Xs.shape
        nt = Xt.shape[0]
        Xs,Xt = scale(Xs,with_std=False),scale(Xt,with_std=False)
        
        y = np.hstack((ys,yt))
        Ky = np.array(y[:,None]==y,dtype=np.float64)   
 
        if self.sigma is None:
            pairwise_dist = pairwise_distances(Xs,Xt,'sqeuclidean')
            self.sigma = np.sqrt(np.median(pairwise_dist[pairwise_dist!=0]) / 2.0)
        
        # construct objective function 
        def objW(W):
            """
            code from 
            https://stackoverflow.com/questions/47271662/what-is-the-fastest-way-to-compute-an-rbf-kernel-in-python
            """                                   
            WX = anp.vstack((anp.dot(Xs,W[0]),anp.dot(Xt,W[1])))
            WX_norm = anp.sum(WX ** 2, axis = -1)
            K_W = WX_norm[:,None] + WX_norm[None,:] - 2 * anp.dot(WX, WX.T)
                
            H = np.power(np.pi * self.sigma**2,self.dimension / 2.0) * anp.exp(-K_W / (4 * self.sigma**2)) * Ky
            Temp = anp.exp(-K_W / (2 * self.sigma**2)) * Ky
            h = anp.mean(Temp[:ns],axis=0) - anp.mean(Temp[ns:],axis=0)
            
            theta = ala.solve(H + self.lamda * anp.eye(ns + nt),h)
            D = anp.dot(h,theta)                       
            return D

        manifold = manifolds.Product([manifolds.Stiefel(dim, self.dimension),manifolds.Stiefel(dim, self.dimension)])
        problem = pm.Problem(manifold=manifold, cost=objW,verbosity=self.verbosity)
        if Ws is None and Wt is None:
            W = solvers.SteepestDescent(maxiter=self.maxiter).solve(problem) 
        else:
            W = solvers.SteepestDescent(maxiter=self.maxiter).solve(problem,x=[Ws[:,:self.dimension],Wt[:,:self.dimension]])        
        return W
