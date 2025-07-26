using System;

class FindDuplicates
{
    static void Main()
    {
        int[] arr = { 4, 7, 2, 4, 9, 7 };
        Console.WriteLine("Duplicate elements:");

        for (int i = 0; i < arr.Length; i++)
        {
            for (int j = i + 1; j < arr.Length; j++)
            {
                if (arr[i] == arr[j])
                {
                    Console.WriteLine(arr[i]);
                    break;
                }
            }
        }
    }
}
