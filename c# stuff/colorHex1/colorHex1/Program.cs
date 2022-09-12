using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1


{
    class Program
    {
        static void Main(string[] args)
        {
            int redNum, greenNum, blueNum;

            Console.WriteLine("Input RED number: ");
            redNum = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Input Green number: ");
            greenNum = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Input Blue number: ");
            blueNum = Convert.ToInt32(Console.ReadLine());

            string redHex = redNum.ToString("X");
            string greenHex = greenNum.ToString("X");
            string blueHex = blueNum.ToString("X");

            string hexColor = "#" + redHex + greenHex + blueHex;

            Console.WriteLine("Color code: " + hexColor);
            Console.ReadLine();
        }
    }
}
