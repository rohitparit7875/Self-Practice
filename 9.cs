using System;

class Employee
{
    public int Id { get; set; }
    public string Name { get; set; }

    public Employee(int id, string name)
    {
        Id = id;
        Name = name;
    }

    public void Display()
    {
        Console.WriteLine($"Employee ID: {Id}, Name: {Name}");
    }
}

class Program
{
    static void Main()
    {
        Employee emp = new Employee(101, "Rohit");
        emp.Display();
    }
}
