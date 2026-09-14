# \# Part 1: The 2D Geometric Core Foundation

# 

# This sub-module demonstrates how to crack 2-prime modular encryption systems (such as sub-300 digit RSA algorithms) by mapping pure algebraic number theory into 2D coordinate spaces.

# 

# \## 📐 Mathematical Formulation

# 

# Instead of searching for primes through standard division loops, we leverage \*\*Fermat's Factorization Method\*\*, which dictates that any odd integer $N$ can be represented as the difference of two squares:

# $$N = x^2 - y^2 \\implies y^2 + N = x^2$$

# 

# This algebraic equation natively outlines a \*\*right-angled triangle\*\* where:

# \*   The base/height relationships are tied directly to the modular boundaries of $N$.

# \*   The target prime factors are recovered via:

# &#x20;   $$p = x - y, \\quad q = x + y$$

# 

# By converting this into a geometric vector system, an AI agent scans coordinates and locks onto perfect integer intersections (\*\*Point-Snapping\*\*), avoiding brute-force iterations.

# 

# \## 🚀 Getting Started

# 

# Run the localized simulation script to observe how the Pythagorean Snapper dynamically sweeps the coordinate space to locate the prime factors of a target key:

# 

# ```bash

# python rsa\_fermat\_snapper.py

# ```



