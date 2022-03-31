%Esta función logra resolver una matriz triangular superior con el método
%de sustitución hacia atrás.
function x = uppTrMatrix(A, b)
    [m, n] = size(A);
    x = zeros(m, 1);
    x(n) = b(n)/A(n, n);
    for i=n-1:-1:1  #i desde n-1 resta de a -1 hasta 1
        tmp = 0;
        for j=i+1:n
            tmp = tmp + (A(i,j) * x(j));
        end
        x(i) = (b(i) - tmp) / A(i, i);
    end
end