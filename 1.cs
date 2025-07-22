using System;

class Program {
    static void Main() {
        Console.Write("Enter number of terms: ");
        int n = int.Parse(Console.ReadLine());

        int a = 0, b = 1, c;

        Console.WriteLine("Fibonacci Series:");
        for (int i = 0; i < n; i++) {
            Console.Write(a + " ");
            c = a + b;
            a = b;
            b = c;
        }
    }
}
