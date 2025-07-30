using System;
using System.Management;

class SystemInfo
{
    static void Main()
    {
        ManagementObjectSearcher searcher = new ManagementObjectSearcher("select * from Win32_Processor");
        foreach (ManagementObject obj in searcher.Get())
        {
            Console.WriteLine("Processor: " + obj["Name"]);
        }

        searcher = new ManagementObjectSearcher("select * from Win32_OperatingSystem");
        foreach (ManagementObject obj in searcher.Get())
        {
            Console.WriteLine("Total RAM: " + Math.Round(Convert.ToDouble(obj["TotalVisibleMemorySize"]) / 1024, 2) + " MB");
        }
    }
}
