using System;
using System.Collections.Generic;

#nullable disable

namespace ComicBookTracker
{
    public partial class AuthUser
    {
        public AuthUser()
        {
            AuthUserGroups = new HashSet<AuthUserGroup>();
            AuthUserUserPermissions = new HashSet<AuthUserUserPermission>();
            //DjangoAdminLogs = new HashSet<DjangoAdminLog>();
        }

        public long Id { get; set; }
        public string Password { get; set; }
        public byte[] LastLogin { get; set; }
        public byte[] IsSuperuser { get; set; }
        public string Username { get; set; }
        public string FirstName { get; set; }
        public string Email { get; set; }
        public byte[] IsStaff { get; set; }
        public byte[] IsActive { get; set; }
        public byte[] DateJoined { get; set; }
        public string LastName { get; set; }

        public virtual ICollection<AuthUserGroup> AuthUserGroups { get; set; }
        public virtual ICollection<AuthUserUserPermission> AuthUserUserPermissions { get; set; }
        //public virtual ICollection<DjangoAdminLog> DjangoAdminLogs { get; set; }
    }
}
