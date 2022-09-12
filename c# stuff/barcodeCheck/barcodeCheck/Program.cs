using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace barcodeCheck
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter your partial barcode...");
            String upc = Console.ReadLine();
            if (upc.Length > 11)
            {
                throw new Exception("Invalid UPC length");
            }
            else if(upc.Length < 11)
            {
                while (upc.Length < 11)
                    upc = '0' + upc;
            }
            Console.WriteLine("Last digit is " + Checker(upc));
            Console.WriteLine("Full numbers is " + upc + Checker(upc));
            Console.ReadLine();
        }

        static public int Checker(String code)
        {
            int[] numbers = new int[11];
            int counter = 0;

            foreach (char a in code)
            {
                numbers[counter] = int.Parse(a.ToString());
                counter++;
            }

            int sum = numbers[0] + numbers[2] + numbers[4] + numbers[6] + numbers[8] + numbers[10];
            sum = sum * 3;
            sum = sum + (numbers[1] + numbers[3] + numbers[5] + numbers[7] + numbers[9]);

            int m = sum % 10;
            if (m == 0)
                return 0;
            else
                m = 10 - m;

            return m; 
        }
    }
}
