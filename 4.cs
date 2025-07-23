using System;
using System.Threading;

class DigitalClock
{
    static void Main()
    {
        while (true)
        {
            Console.Clear();
            Console.WriteLine(DateTime.Now.ToString("hh:mm:ss tt"));
            Thread.Sleep(1000);
        }
    }
}
