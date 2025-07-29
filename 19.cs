using System;

class Program {
    static void Main() {
        Console.Write("Enter a string: ");
        string input = Console.ReadLine();
        string reversed = ReverseString(input);
        Console.WriteLine("Reversed: " + reversed);
    }

    static string ReverseString(string str) {
        char[] charArray = str.ToCharArray();
        Array.Reverse(charArray);
        return new string(charArray);
    }
}
