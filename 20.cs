using System;

class Program {
    static void Main() {
        Console.Write("Enter a number: ");
        int num = Convert.ToInt32(Console.ReadLine());
        bool isPrime = IsPrime(num);
        Console.WriteLine(isPrime ? "Prime Number" : "Not a Prime Number");
    }

    static bool IsPrime(int number) {
        if (number <= 1) return false;
        for (int i = 2; i <= Math.Sqrt(number); i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
}
