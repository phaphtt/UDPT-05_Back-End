using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using MySql.Data;
using MySql.Data.MySqlClient;
using System.Data;

namespace HRM.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class Employee : Controller
    {
        [HttpGet("getInfor/{id}")]
        public IEnumerable<Models.InforDetailEmployee> GetInforEmployee(int id)
        {
            //Connect DB:
            Models.MySQLsetting.ConnectToMySqlService();
            string procedure = "GetInforEmployeeById";
            MySqlCommand cmd = new MySqlCommand(procedure, Models.MySQLsetting.conn);
            cmd.CommandType = CommandType.StoredProcedure;
            cmd.Parameters.AddWithValue("@id", id);
            MySqlDataReader result = cmd.ExecuteReader();

            if (result.HasRows)
            {
                while (result.Read())
                {
                    Models.InforDetailEmployee employee = new Models.InforDetailEmployee();
                    employee.id = result.GetInt32("id");
                    if (!result.IsDBNull(1))
                        employee.idManager = result.GetInt32("idManager");
                    if (!result.IsDBNull(2))
                        employee.idDepartment = result.GetInt32("idDepartment");
                    if (!result.IsDBNull(3))
                        employee.idEmployee = result.GetString("idEmployee");
                    if (!result.IsDBNull(4))
                        employee.firstname = result.GetString("firstname");
                    if (!result.IsDBNull(5))
                        employee.lastname = result.GetString("lastname");
                    if (!result.IsDBNull(6))
                        employee.dayOfBirth = result.GetString("dayOfBirth");
                    if (!result.IsDBNull(7))
                        employee.gender = result.GetString("gender");
                    if (!result.IsDBNull(8))
                        employee.email = result.GetString("email");
                    if (!result.IsDBNull(9))
                        employee.phoneNumber = result.GetString("phoneNumber");
                    if (!result.IsDBNull(10))
                        employee.address = result.GetString("address");
                    if (!result.IsDBNull(11))
                        employee.maritalStatus = result.GetString("maritalStatus");
                    if (!result.IsDBNull(12))
                        employee.position = result.GetString("position");
                    if (!result.IsDBNull(13))
                        employee.active = result.GetInt32("active");
                    if (!result.IsDBNull(14))
                        employee.manager_idEmployee = result.GetString("manager_idEmployee");
                    if (!result.IsDBNull(15))
                        employee.manager_firstname = result.GetString("manager_firstname");
                    if (!result.IsDBNull(16))
                        employee.manager_lastname = result.GetString("manager_lastname");
                    if (!result.IsDBNull(17))
                        employee.manager_gender = result.GetString("manager_gender");
                    if (!result.IsDBNull(18))
                        employee.manager_idDepartment = result.GetInt32("manager_idDepartment");
                    if (!result.IsDBNull(19))
                        employee.manager_position = result.GetString("manager_position");
                    if (!result.IsDBNull(20))
                        employee.manager_email = result.GetString("manager_email");
                    if (!result.IsDBNull(21))
                        employee.manager_phoneNumber = result.GetString("manager_phoneNumber");
                    yield return employee;
                }
            }
        }
    }
}
