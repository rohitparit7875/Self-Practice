using System;

class Program {
    static void Main() {
        int[] numbers = { 12, 45, 7, 89, 34 };
        int max = FindMax(numbers);
        Console.WriteLine("Largest number is: " + max);
    }

    static int FindMax(int[] arr) {
        int max = arr[0];
        foreach (int num in arr) {
            if (num > max)
                max = num;
        }
        return max;
    }
}
