import subprocess

equations = ["5 + 4 * X + X^2= X^2",
            "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
            "5 * X^0 + 4 * X^1 = 4 * X^0",
            "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
            "42 * X^0 = 42 * X^0",
            "1 .2 * X^0 + 4 * X^1 = 4 * X^0"]

print("\n\n---- COMPUTOR V1 TESTS ----\n")
for equation in equations:
    print(f"Testing: {equation}")
    subprocess.run(["python", "computor.py", equation])
    print("\n")

#tester