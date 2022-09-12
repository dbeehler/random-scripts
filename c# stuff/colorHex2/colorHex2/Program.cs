using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using System.Threading.Tasks;

namespace colorHex2
{
    class Program
    {
        static void Main(string[] args)
        {
            String final = "";
            String rgbTogether= "";
            Console.WriteLine("Enter a RGB string");
            String input = Console.ReadLine();
            String[] numbers = input.Split(' ');
            int[] numbersSplit = Array.ConvertAll(numbers, int.Parse);
            for(int x = 0; x < 3; x++)
            {
                rgbTogether += numbersSplit[x];
                final += numbersSplit[x].ToString("X");
            }
            Console.WriteLine(final);
            Console.ReadLine();
        }
    }
}
