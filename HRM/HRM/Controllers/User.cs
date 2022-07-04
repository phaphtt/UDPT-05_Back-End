using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using MySql.Data;
using MySql.Data.MySqlClient;

namespace HRM.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class User : Controller
    {
        // GET: api/user/getall
        [HttpGet("getAll")]
        public IEnumerable<Models.User> GetAllUser()
        {
            //Connect DB:
            Models.MySQLsetting.ConnectToMySqlService();
            string sql = "SELECT username, password FROM user";
            MySqlCommand cmd = new MySqlCommand(sql, Models.MySQLsetting.conn);
            MySqlDataReader result = cmd.ExecuteReader();

            if (result.HasRows)
            {
                while (result.Read())
                {
                    Models.User user = new Models.User();
                    user.username = result.GetString("username");
                    if (!result.IsDBNull(1))
                        user.password = result.GetString("password");
                    yield return user;
                }
            }
        }
    }
}
