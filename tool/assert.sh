pwd
cd ./tool
while true; do
    python random_array.py > input.txt
    actual=$(python assert.py < input.txt)
    exit_code=$? # cache sys.exit(1)
    if [ $exit_code -eq 1 ]; then
        echo "Wrong Answer"
        echo "Input:"
        cat input.txt
        echo "Actual:" $actual
    fi
done
