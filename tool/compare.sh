pwd
cd ./tool
while true; do
    python random_array.py > input.txt
    actual=$(python solve_actual.py < input.txt)
    expected=$(python solve_expected.py < input.txt)
    if [ $actual != $expected ]; then
        echo "Wrong Answer"
        echo "Input:"
        cat input.txt
        echo "Actual:" $actual
        echo "Expected:" $expected
        exit
    fi
done
