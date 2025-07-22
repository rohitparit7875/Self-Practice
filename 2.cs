using System;

class Program {
    static void Main() {
        Console.Write("Enter a number: ");
        int num = int.Parse(Console.ReadLine());
        bool isPrime = true;

        if (num <= 1)
            isPrime = false;
        else {
            for (int i = 2; i <= Math.Sqrt(num); i++) {
                if (num % i == 0) {
                    isPrime = false;
                    break;
                }
            }
        }

        Console.WriteLine(isPrime ? "Prime Number" : "Not a Prime Number");
    }
}
