# JDIP
Joint Distribution Invariant Projections (JDIP) implemented in Python

## Visual and Semantic OPtimization (VSOP)

A demo application running on the AWA1 data set  
Joint Visual and Semantic Optimization for Zero-shot Learning, Knowledge-Based Systems, 2021 [[pdf](https://www.sciencedirect.com/science/article/abs/pii/S0950705121000368?via%3Dihub)]  
Authors: Hanrui Wu, Yuguang Yan, Sentao Chen, Xiangkang Huang, Qingyao Wu, Michael K. Ng  
Please note that the initialization of the mapping matrices P and Q has an impact on the result.  

An illustration of the proposed VSOP method  
![procedure](procedure.png)

The codes are written based on the ManOpt provided by Z. Wen and W. Yin. A feasible method for optimization with orthogonality constraints. Mathematical Programming 2013  
The data are provied by Xian Y, Lampert C H, Schiele B, et al. Zero-shot learning -- A comprehensive evaluation of the good, the bad and the ugly. IEEE TPAMI 2018  

Please cite our paper if you find this code helpful to your research:  
@article{wu2021joint,  
title = {Joint Visual and Semantic Optimization for zero-shot learning},  
journal = {Knowledge-Based Systems},  
volume = {215},  
pages = {106773},  
year = {2021},  
doi = {https://doi.org/10.1016/j.knosys.2021.106773},  
author = {Hanrui, Wu and Yuguang, Yan and Sentao, Chen and Xiangkang, Huang and Qingyao, Wu and Michael, K. Ng}  
}

