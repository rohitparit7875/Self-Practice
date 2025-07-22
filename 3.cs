using System;

class Program {
    static void Main() {
        Console.Write("Enter a string: ");
        string input = Console.ReadLine();

        char[] chars = input.ToCharArray();
        Array.Reverse(chars);
        string reversed = new string(chars);

        Console.WriteLine("Reversed String: " + reversed);
    }
}
