function oj-test
    set problem (string split / $argv)[1]
    oj t -c "python3 $problem/main.py" -d ./$problem/tests/
end
