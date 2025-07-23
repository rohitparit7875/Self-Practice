using System;

class PasswordGenerator
{
    static void Main()
    {
        const string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%";
        Random rand = new Random();
        Console.Write("Enter password length: ");
        int length = int.Parse(Console.ReadLine());
        string password = "";

        for (int i = 0; i < length; i++)
        {
            password += chars[rand.Next(chars.Length)];
        }

        Console.WriteLine($"Generated Password: {password}");
    }
}
