%Esta función logra resolver una matriz triangular inferior con el método
%de sustitución hacia adelante.
function x = lowTrMatrix(A, b)
    [m, n] = size(A);  #m = filas, n = colum
    x = zeros(m, 1); #x = np.zeros
    x(1) = b(1)/A(1, 1);  # x[0] = b [0] / A[0][0]
    for i=2:n #inicio desde 1 hasta n + 1
        tmp = 0;
        for j=1:i-1
            tmp = tmp + (A(i,j) * x(j));
        end
        x(i) = (b(i) - tmp) / A(i, i);
    end
end