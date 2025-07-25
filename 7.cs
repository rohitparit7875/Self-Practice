using System;

class Program
{
    static void Main()
    {
        string input = "dotnet";
        string reversed = "";

        for (int i = input.Length - 1; i >= 0; i--)
        {
            reversed += input[i];
        }

        Console.WriteLine("Reversed string: " + reversed);
    }
}
