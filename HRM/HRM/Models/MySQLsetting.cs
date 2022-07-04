using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace HRM.Models
{
    public class MySQLsetting
    {
        public static string myConnectionString = "server=sql6.freemysqlhosting.net;uid=sql6503851;pwd=ZnymiZ3f13;port=3306;database=sql6503851";
        public static MySqlConnection conn { get; set; }
        internal static void ConnectToMySqlService()
        {
            try
            {
                conn = new MySqlConnection();
                conn.ConnectionString = myConnectionString;
                conn.Open();
            }
            catch
            {
                throw;
            }
        }
    }
}
