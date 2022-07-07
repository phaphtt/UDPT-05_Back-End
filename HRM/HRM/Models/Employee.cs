using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace HRM.Models
{
    public class Employee
    {
        public int id { get; set; }
        public int idManager { get; set; }
        public int idDepartment { get; set; }
        public string idEmployee { get; set; }
        public string firstname { get; set; }
        public string lastname { get; set; }
        public string dayOfBirth { get; set; }
        public string gender { get; set; }
        public string email { get; set; }
        public string phoneNumber { get; set; }
        public string address { get; set; }
        public string maritalStatus { get; set; }
        public string position { get; set; }
        public int active { get; set; }
    }

    public class InforDetailEmployee : Employee
    {
        public int manager_idDepartment { get; set; }
        public string manager_idEmployee { get; set; }
        public string manager_firstname { get; set; }
        public string manager_lastname { get; set; }
        public string manager_gender { get; set; }
        public string manager_email { get; set; }
        public string manager_phoneNumber { get; set; }
        public string manager_position { get; set; }
    }
}
