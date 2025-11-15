using System;
class Program {
    static void Main(string[] args) {
        double R = double.Parse(Console.ReadLine());
        double A = 3.14159 * R * R;
        Console.WriteLine($"A={A:F4}");
    }
}