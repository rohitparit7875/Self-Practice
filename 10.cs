using System;

class MaxMinArray
{
    static void Main()
    {
        int[] numbers = { 15, 2, 89, 45, 7 };
        int max = numbers[0], min = numbers[0];

        foreach (int num in numbers)
        {
            if (num > max) max = num;
            if (num < min) min = num;
        }

        Console.WriteLine("Maximum: " + max);
        Console.WriteLine("Minimum: " + min);
    }
}
