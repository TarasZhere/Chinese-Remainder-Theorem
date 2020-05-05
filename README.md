# Chinese-Remainder-Theorem
These is a simple CRT calculator
Let n1, ..., nk be integers greater than 1, which are often called moduli or divisors. Let us denote by N the product of the ni.

The Chinese remainder theorem asserts that if the ni are pairwise coprime, and if a1, ..., ak are integers such that 0 ≤ ai < ni for every i, then there is one and only one integer x, such that 0 ≤ x < N and the remainder of the Euclidean division of x by ni is ai for every i.

This may be restated as follows in term of congruences: If the ni are pairwise coprime, and if a1, ..., ak are any integers, then there exist integers x such that

    x ≡ a1 ( mod n1 ) 
    ⋮ 
    x ≡ ak ( mod nk )

and any two solutions, say x1 and x2, are congruent modulo N, that is, x1 ≡ x2 (mod N).

In abstract algebra, the theorem is often restated as: if the ni are pairwise coprime, the map

    x mod N ↦ ( x mod n1 , … , x mod nk )

defines a ring isomorphism

    Z / N Z ≅ Z / n 1 Z × ⋯ × Z / nk Z 

between the ring of integers modulo N and the direct product of the rings of integers modulo the ni. This means that for doing a sequence of arithmetic operations in Z / N Z , and then get the result by applying the isomorphism (from the right to the left). This may be much faster than the direct computation if N and the number of operations are large. This is widely used, under the name multi-modular computation, for linear algebra over the integers or the rational numbers.

The theorem can also be restated in the language of combinatorics as the fact that the infinite arithmetic progressions of integers form a Helly family.
