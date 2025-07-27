using System;

class ReverseWords
{
    static void Main()
    {
        Console.Write("Enter a sentence: ");
        string sentence = Console.ReadLine();

        string[] words = sentence.Split(' ');
        Array.Reverse(words);

        string reversed = string.Join(" ", words);
        Console.WriteLine("Reversed sentence: " + reversed);
    }
}
