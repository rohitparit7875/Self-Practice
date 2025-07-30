using System;
using System.IO;

class CSVWriter
{
    static void Main()
    {
        string path = "data.csv";
        using (StreamWriter sw = new StreamWriter(path))
        {
            sw.WriteLine("Name,Age,Email");
            for (int i = 0; i < 3; i++)
            {
                Console.Write("Enter Name: ");
                string name = Console.ReadLine();
                Console.Write("Enter Age: ");
                string age = Console.ReadLine();
                Console.Write("Enter Email: ");
                string email = Console.ReadLine();

                sw.WriteLine($"{name},{age},{email}");
            }
        }
        Console.WriteLine("CSV file 'data.csv' created.");
    }
}
